const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();

app.use(express.json());
app.use(express.static("public"));

app.post("/predict", async (req, res) => {
  const input_data = req.body.data;
  try {
    const response = await axios.post("http://locahost:5000/predict", {
      data: input_data,
    });
    res.json({ prediction: response.data.prediction });
  } catch (error) {
    console.log(`the error is ${error}`);
  }
});

app.listen(3000, () => {
  console.log(`app is running on http://localhost:3000`);
});
