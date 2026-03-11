function TaskTable({tasks,toggleTask,deleteTask}){

  return(

    <table border="1">

      <thead>
        <tr>
          <th>Title</th>
          <th>Priority</th>
          <th>Completed</th>
          <th>Action</th>
        </tr>
      </thead>

      <tbody>

      {tasks.map(t => (

        <tr key={t.id}>

          <td>{t.title}</td>
          <td>{t.priority}</td>

          <td>
            <input
              type="checkbox"
              checked={t.completed}
              onChange={()=>toggleTask(t.id)}
            />
          </td>

          <td>
            <button onClick={()=>deleteTask(t.id)}>
              Delete
            </button>
          </td>

        </tr>

      ))}

      </tbody>

    </table>

  );

}

export default TaskTable;
