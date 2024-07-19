const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static files from the 'public' directory
app.use(express.static("public"));

// Endpoint to handle predictions
app.post("/predict", async (req, res) => {
  const inputData = req.body.data;
  try {
    console.log(`Sending data to Flask server: ${inputData}`);
    const response = await axios.post("http://127.0.0.1:5000/predict", {
      data: inputData,
    });
    const prediction = response.data.prediction;
    res.redirect(`/result?prediction=${prediction}`);
  } catch (error) {
    console.error(`Error in /predict endpoint: ${error.message}`);
    res.status(500).send("Error in fetching prediction");
  }
});

// Endpoint to serve result page
app.get("/result", (req, res) => {
  const prediction = req.query.prediction;
  res.send(`
        <h1>Prediction Result</h1>
        <p>Prediction: ${prediction}</p>
        <a href="/">Go back</a>
    `);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
