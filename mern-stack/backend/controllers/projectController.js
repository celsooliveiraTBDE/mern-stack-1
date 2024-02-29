// Import required modules
const Project = require('../models/project');

// Controller functions for project management
const ProjectController = {
  // Get all projects
  getProjects: async (req, res) => {
    try {
      const projects = await Project.find();
      res.json(projects);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },

  // Create a new project
  createProject: async (req, res) => {
    try {
      const newProject = await Project.create(req.body);
      res.status(201).json(newProject);
    } catch (error) {
      res.status(400).json({ message: error.message });
    }
  },

  // Update an existing project
  updateProject: async (req, res) => {
    try {
      const updatedProject = await Project.findByIdAndUpdate(req.params.id, req.body, { new: true });
      res.json(updatedProject);
    } catch (error) {
      res.status(400).json({ message: error.message });
    }
  },

  // Delete a project
  deleteProject: async (req, res) => {
    try {
      await Project.findByIdAndDelete(req.params.id);
      res.json({ message: 'Project deleted successfully' });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  }
};

module.exports = ProjectController;
