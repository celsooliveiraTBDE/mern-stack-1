// Import required modules
const express = require('express');
const ProjectController = require('../controllers/projectController');

// Create a router instance
const router = express.Router();

// Define routes for project management
router.get('/projects', ProjectController.getProjects); // Get all projects
router.post('/projects', ProjectController.createProject); // Create a new project
router.put('/projects/:id', ProjectController.updateProject); // Update an existing project
router.delete('/projects/:id', ProjectController.deleteProject); // Delete a project

module.exports = router;
