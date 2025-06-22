const express = require("express")
const cors = require("cors")
const mongoose = require("mongoose")
const userRouter = require("./routes/user")
require("dotenv").config()
const app = express()

mongoose.connect(process.env.MONGO_DB_URL)
    .then(() => console.log("Connexion à MongoDB réussie !"))
    .catch(() => console.log("Échec de la connexion à MongoDB !"))

app.use(cors())
app.use(express.json())

app.use("/auth", userRouter)
app.use((req, res) => {
    res.status(404).json({message: "Route Introuvable !"})
})

module.exports = app
