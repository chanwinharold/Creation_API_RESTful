const express = require("express")
const contactCtrl = require("../controllers/contact")
const router = express.Router()
const auth = require("../middlewares/auth")


router.post('/', auth, contactCtrl.createContact)
router.get('/', auth, contactCtrl.getAllContact)
router.get('/:id', auth, contactCtrl.getOneContact)
router.put('/:id', auth, contactCtrl.modifyContact)
router.delete('/:id', auth, contactCtrl.deleteContact)

module.exports = router