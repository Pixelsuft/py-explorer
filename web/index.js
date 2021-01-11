var result;
async function change_dir_js(){
	if(await eel.py_change_dir(document.getElementById('path').value)()==true)location.reload();
}
async function change_dir_js_func(pathed){
	if(await eel.py_change_dir(document.getElementById('path').value+'\\'+pathed)()==true)location.reload();
}
async function k(e){
	if(e.key=="Enter")await change_dir_js();
}
async function go_back(){
	document.getElementById('path').value+='\\..';
	await change_dir_js();
}
function add(mas){
	var z='';
	z='<div class="files" id="'+mas[0]+'">';
	if(mas[0]=='..' && mas[1]==true)
	{
		mas[0]='Go Back';
		z+='<img class="files_img" src="img/go_back.png">';
	}
	else if(mas[1]==true)z+='<img class="files_img" src="img/folder.png">';
	z+=mas[0];
	z+='</div>';
	document.getElementById('root').innerHTML+=z;
}
async function list_js(){
	result=await eel.py_list_dir()();
	for(var i=1;i<result.length;i++)
	{
		add(result[i]);
		console.log(result[i]);
	}
	document.getElementById('path').value=result[0];
	document.title='Py Explorer ('+result[0]+')';
	document.getElementById('..').onclick=async function(){
		await change_dir_js_func('..');
	};
}
list_js();