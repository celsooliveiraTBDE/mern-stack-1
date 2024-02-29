// Import required modules
const express = require('express');

// Create a router instance
const router = express.Router();

// Import and mount route handlers
const userRoutes = require('./userRoutes');
const projectRoutes = require('./projectRoutes');

// Mount user routes
router.use('/users', userRoutes);

// Mount project routes
router.use('/projects', projectRoutes);

// Export the router
module.exports = router;