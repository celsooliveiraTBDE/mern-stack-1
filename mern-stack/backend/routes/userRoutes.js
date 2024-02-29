// Import required modules
const express = require('express');
const UserController = require('../controllers/userController');

// Create a router instance
const router = express.Router();

// Define routes for user management
router.get('/users', UserController.getUsers); // Get all users
router.post('/users', UserController.createUser); // Create a new user
router.put('/users/:id', UserController.updateUser); // Update an existing user
router.delete('/users/:id', UserController.deleteUser); // Delete a user

module.exports = router;
