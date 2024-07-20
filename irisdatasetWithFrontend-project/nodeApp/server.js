const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());
app.use(express.static("public"));
app.post("/prediction", async (req, res) => {
  try {
    const response = await axios.post("http://localhost:5000/predict", {
      features: req.body.features,
    });
    res.json(response.data);
  } catch (error) {
    console.log(`error : ${error}`);
  }
});

app.listen(3000, () => {
  console.log("app is running on http://localhost:3000");
});
