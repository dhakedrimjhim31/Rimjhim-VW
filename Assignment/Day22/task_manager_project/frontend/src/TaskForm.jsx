import { useState } from "react";
import { createTask } from "./api";

function TaskForm({ reload }) {

  const [title,setTitle] = useState("");
  const [priority,setPriority] = useState("Low");

  const submit = async(e)=>{
    e.preventDefault();

    await createTask({title,priority});

    setTitle("");
    reload();
  };

  return (

    <form onSubmit={submit}>

      <input
        placeholder="Task Title"
        value={title}
        onChange={(e)=>setTitle(e.target.value)}
      />

      <select
        value={priority}
        onChange={(e)=>setPriority(e.target.value)}
      >
        <option>Low</option>
        <option>Medium</option>
        <option>High</option>
      </select>

      <button>Add Task</button>

    </form>
  );
}

export default TaskForm;