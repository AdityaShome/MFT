const express = require("express");
const app = express();

app.get("/api", (req, res) => {
  res.json({ message: "API works!" });
});

app.listen(3000, () => console.log("Server running"));
