const express = require("express")
const app = express()
const mongoose = require("mongoose")
const taskRoutes = require("./routes/tasks")

mongoose.connect("mongodb+srv://<user>:<password>@cluster0.44esyvl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    .then(() => console.log("✅ Connexion réussie"))
    .catch(() => console.log("❌ Connexion échouée"))

app.use(express.json())

app.use("/tasks", taskRoutes)

app.use((req, res) => {
    res.status(404).json({ message: "Route introuvable !" });
});

module.exports = app