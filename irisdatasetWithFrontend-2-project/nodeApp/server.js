const express = require("express");
const axios = require("axios");
const path = require("path");
const bodyParser = require("body-parser");

const app = express();

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, "public")));

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Route to handle data forwarding from the frontend
app.post("/send-to-flask", async (req, res) => {
  try {
    const response = await axios.post("http://localhost:5000/predict", {
      features: req.body.features,
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Start the server
app.listen(3000, () => {
  console.log("Node.js server running on port 3000");
});
