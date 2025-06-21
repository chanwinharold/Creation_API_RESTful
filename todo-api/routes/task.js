const express = require("express")
const router = express.Router()
const taskController = require("../controllers/task")

router.post("/", taskController.createTask)
router.get("/", taskController.getAllTask)
router.get("/:id", taskController.getOneTask)
router.put("/:id", taskController.modifyTask)
router.delete("/:id", taskController.deleteTask)

module.exports = router