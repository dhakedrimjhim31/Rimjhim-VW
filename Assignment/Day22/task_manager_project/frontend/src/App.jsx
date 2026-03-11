import {useState,useEffect} from "react";
import TaskForm from "./TaskForm";
import TaskTable from "./TaskTable";
import Filters from "./Filters";
import {getTasks,toggleTask,deleteTask} from "./api";

function App(){

  const [tasks,setTasks] = useState([]);
  const [priority,setPriority] = useState("");
  const [completed,setCompleted] = useState(false);

  const loadTasks = async()=>{

    const params={};

    if(priority) params.priority=priority;
    if(completed) params.completed=true;

    const res = await getTasks(params);

    setTasks(res.data);
  };

  useEffect(()=>{
    loadTasks();
  },[priority,completed]);

  return(

    <div>

      <h1>Task Manager</h1>

      <TaskForm reload={loadTasks}/>

      <Filters
        priority={priority}
        setPriority={setPriority}
        completed={completed}
        setCompleted={setCompleted}
      />

      <TaskTable
        tasks={tasks}
        toggleTask={async(id)=>{
          await toggleTask(id);
          loadTasks();
        }}
        deleteTask={async(id)=>{
          await deleteTask(id);
          loadTasks();
        }}
      />

    </div>

  );

}

export default App;