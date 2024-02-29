const mongoose = require('mongoose');

const projectSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String },
  technologies: [{ type: String }],
  githubUrl: { type: String },
  demoUrl: { type: String },
  createdBy: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }

});

const Project = mongoose.model('Project', projectSchema);

module.exports = Project;