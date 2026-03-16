import { useState } from "react";

function AssetList(){

const[search,setSearch]=useState("");

const[assets,setAssets]=useState([
{name:"Laptop",brand:"Dell",status:"Assigned"},
{name:"Printer",brand:"HP",status:"Available"}
]);

function deleteAsset(index){

const updated = assets.filter((_,i)=>i!==index);

setAssets(updated);

}

return(

<div>

<h2>Assets</h2>

<input
placeholder="Search asset"
onChange={(e)=>setSearch(e.target.value)}
/>

<table>

<thead>

<tr>
<th>Name</th>
<th>Brand</th>
<th>Status</th>
<th>Action</th>
</tr>

</thead>

<tbody>

{assets.filter(a=>a.name.includes(search)).map((a,i)=>(

<tr key={i}>

<td>{a.name}</td>
<td>{a.brand}</td>
<td>{a.status}</td>

<td>
<button onClick={()=>deleteAsset(i)}>
Delete
</button>
</td>

</tr>

))}

</tbody>

</table>

</div>

)

}

export default AssetList