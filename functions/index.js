const { onCall, HttpsError } = require('firebase-functions/v2/https');
const { onDocumentWritten } = require('firebase-functions/v2/firestore');
const admin = require('firebase-admin');

admin.initializeApp();
const db = admin.firestore();

function canEdit(auth) {
  return auth && (auth.token.admin === true || auth.token.editor === true);
}

exports.searchPublishedResources = onCall(async (request) => {
  const { text = '', resourceType = null, competency = null, stage = null, limit = 30 } = request.data || {};
  const safeLimit = Math.min(Math.max(Number(limit) || 30, 1), 100);
  let query = db.collection('resources').where('status', '==', 'published').limit(safeLimit);
  if (resourceType) query = query.where('resourceType', '==', resourceType);
  if (competency) query = query.where('selCompetencies', 'array-contains', competency);
  if (stage) query = query.where('educationStages', 'array-contains', stage);
  const snap = await query.get();
  const term = String(text).trim().toLocaleLowerCase();
  return snap.docs.map(d => ({ id: d.id, ...d.data() })).filter(x => !term || [x.title, x.abstractSummary, x.source].join(' ').toLocaleLowerCase().includes(term));
});

exports.setUserRole = onCall(async (request) => {
  if (!request.auth || request.auth.token.admin !== true) throw new HttpsError('permission-denied', 'Admin role required.');
  const { uid, role } = request.data || {};
  if (!uid || !['admin','editor','reviewer','teacher'].includes(role)) throw new HttpsError('invalid-argument', 'Invalid uid or role.');
  const claims = role === 'admin' ? { admin: true, editor: true, reviewer: true } : role === 'editor' ? { editor: true } : role === 'reviewer' ? { reviewer: true } : {};
  await admin.auth().setCustomUserClaims(uid, claims);
  await db.collection('users').doc(uid).set({ role, updatedAt: admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
  return { ok: true, uid, role };
});

exports.auditResourceChanges = onDocumentWritten('resources/{resourceId}', async (event) => {
  const before = event.data.before.exists ? event.data.before.data() : null;
  const after = event.data.after.exists ? event.data.after.data() : null;
  await db.collection('auditLogs').add({ collection: 'resources', resourceId: event.params.resourceId, action: !before ? 'create' : !after ? 'delete' : 'update', before, after, changedAt: admin.firestore.FieldValue.serverTimestamp() });
});

