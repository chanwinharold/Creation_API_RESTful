const express = require("express")
const router = express.Router()
const taskController = require("../controllers/task")
const auth = require("../middlewares/auth")

router.post("/", auth, taskController.createTask)
router.get("/", auth, taskController.getAllTask)
router.get("/:id", auth, taskController.getOneTask)
router.put("/:id", auth, taskController.modifyTask)
router.delete("/:id", auth, taskController.deleteTask)

module.exports = router