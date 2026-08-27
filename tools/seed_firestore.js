const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const projectId = process.env.FIREBASE_PROJECT_ID || 'sel-database-2a325';
const credentialPath = process.env.GOOGLE_APPLICATION_CREDENTIALS;
if (!credentialPath) throw new Error('Set GOOGLE_APPLICATION_CREDENTIALS to a Firebase service-account JSON path.');
admin.initializeApp({ credential: admin.credential.cert(require(path.resolve(credentialPath))), projectId });
const db = admin.firestore();
const plan = path.join(__dirname, '..', 'SEL平台規劃');
const resources = JSON.parse(fs.readFileSync(path.join(plan, '18_SEL資源摘要索引.json'), 'utf8'));
const competencies = JSON.parse(fs.readFileSync(path.join(plan, '19_SEL五大核心能力說明.json'), 'utf8'));
const media = JSON.parse(fs.readFileSync(path.join(plan, '20_影音與網站資源.json'), 'utf8'));

function resourceDoc(x) {
  return { legacyId:x.resource_id, title:x.title, abstractSummary:x.abstract_summary, resourceType:x.resource_type, selCompetencies:x.sel_core_competency.split(';'), educationStages:x.education_stage.split(';'), curriculumIssue:x.curriculum_108_issue, source:x.source, sourceUrl:x.source_url, licenseOrAccess:x.license_or_access, verificationStatus:x.verification_status, notes:x.notes, status:'draft', updatedAt:admin.firestore.FieldValue.serverTimestamp() };
}
async function run() {
  const batch = db.batch();
  for (const x of resources) batch.set(db.collection('resources').doc(x.resource_id), resourceDoc(x));
  for (const x of competencies) batch.set(db.collection('competencies').doc(x.id), { name:x.name, definition:x.definition, teacherFocus:x.teacher_focus, classroomEntry:x.classroom_entry, updatedAt:admin.firestore.FieldValue.serverTimestamp() });
  for (const x of media) batch.set(db.collection('mediaResources').doc(x.resource_id), { ...x, status:'draft', updatedAt:admin.firestore.FieldValue.serverTimestamp() });
  await batch.commit();
  console.log(`Seeded ${resources.length} resources, ${competencies.length} competencies, ${media.length} media resources as draft.`);
}
run().catch(err => { console.error(err); process.exit(1); });

