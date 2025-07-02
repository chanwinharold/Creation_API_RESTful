const express = require("express")
const contactCtrl = require("../controllers/contact")
const router = express.Router()


router.post('/', contactCtrl.createContact)
router.get('/', contactCtrl.getAllContact)
router.get('/:id', contactCtrl.getOneContact)
router.put('/:id', contactCtrl.modifyContact)
router.delete('/:id', contactCtrl.deleteContact)

module.exports = router