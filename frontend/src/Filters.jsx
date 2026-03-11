function Filters({priority,setPriority,completed,setCompleted}){

  return(

    <div>

      <select
        value={priority}
        onChange={(e)=>setPriority(e.target.value)}
      >
        <option value="">All Priority</option>
        <option value="Low">Low</option>
        <option value="Medium">Medium</option>
        <option value="High">High</option>
      </select>

      <label>

        <input
          type="checkbox"
          checked={completed}
          onChange={(e)=>setCompleted(e.target.checked)}
        />

        Completed

      </label>

    </div>
  );

}

export default Filters;