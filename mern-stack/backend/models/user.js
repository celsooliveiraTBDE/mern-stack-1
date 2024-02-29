const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  bio: { type: String },
  skills: [{ type: String }],
  social: {
    github: { type: String },
    linkedin: { type: String },
    twitter: { type: String }
  }
});

const User = mongoose.model('User', userSchema);

module.exports = User;
