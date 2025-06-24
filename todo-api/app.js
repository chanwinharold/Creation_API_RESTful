const express = require("express")
const mongoose = require("mongoose")
const taskRouter = require("./routes/task")
const userRouter = require("./routes/user")
const app = express()

require("dotenv").config()
const MONGO_DB_URL = process.env.MONGO_DB_URL


mongoose.connect(MONGO_DB_URL)
    .then(() => console.log("✅ Connexion réussie"))
    .catch(() => console.log("❌ Connexion échouée"))

app.use(express.json())

app.use("/tasks", taskRouter)
app.use("/auth", userRouter)

app.use((req, res) => {
    res.status(404).json({ message: "Route introuvable !" });
});

module.exports = app