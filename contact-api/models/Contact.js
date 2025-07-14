const mongoose = require("mongoose")
const uniqueValidator = require("mongoose-unique-validator")

const contactSchema = new mongoose.Schema({
    prenom: { type: String, required: true },
    nom: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    tel: { type: String, required: true, unique: true },
    favori: { type: Boolean, required: true },
    userId: { type: String, required: true }
})
contactSchema.plugin(uniqueValidator)

module.exports = mongoose.model("Contact", contactSchema)