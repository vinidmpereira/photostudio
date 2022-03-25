var doc_1 = document.getElementById('id_doc_1');
var doc_2 = document.getElementById('id_doc_2');
var doc_3 = document.getElementById('id_doc_3');
var doc_4 = document.getElementById('id_doc_4');
var doc_5 = document.getElementById('id_doc_5');
var d1_filename = document.getElementById('id_d1_filename');
var d2_filename = document.getElementById('id_d2_filename');
var d3_filename = document.getElementById('id_d3_filename');
var d4_filename = document.getElementById('id_d4_filename');
var d5_filename = document.getElementById('id_d5_filename');
var progress_doc_1 = $('#progress_doc_1');
var progress_doc_2 = $('#progress_doc_2');
var progress_doc_3 = $('#progress_doc_3');
var progress_doc_4 = $('#progress_doc_4');
var progress_doc_5 = $('#progress_doc_5');



function s3_upload(input_field,return_field, progress) {
  input_field.onchange = function(){
    let file = input_field.files[0];
    // let file = input_field.prop('files')[0];
    
    if(!file){
      return alert("No file selected.");
    }
    getSignedRequest(input_field, file ,return_field, progress);
  };
};
function getSignedRequest(input_field,file,return_field, progress){
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/amazon/sign_s3?file_name="+file.name+"&file_type="+file.type);
  xhr.onreadystatechange = function(){
    if(xhr.readyState === 4){
      if(xhr.status === 200){
        var response = JSON.parse(xhr.responseText);
        uploadFile(input_field, file, response.data, response.url, response.filename, return_field, progress);
      }
      else{
        alert("Could not get signed URL.");

      }
    }
  };
  xhr.send();
}
function uploadFile(input_field,file, s3Data, url, filename,return_field, progress){
  var xhr = new XMLHttpRequest();
  xhr.open("POST", s3Data.url);
  var progressBar = progress;
  progressBar.progress({
    total : 100,
    text: {
      active: 'Fazendo upload { value } de { total }',
      success: 'Arquivo carregado com sucesso.'
    }

  })
  xhr.upload.onprogress = function (e) {

    if (e.lengthComputable) {
        let percentComplete = e.loaded / e.total;
        percentComplete = parseInt(percentComplete*100)
        progressBar.progress({
          value : percentComplete
        })
      }
  }
  // xhr.upload.onloadstart = function (e) {
  //     progressBar.value = 0;
  // }
  // xhr.upload.onloadend = function (e) {
  //     progressBar.value = e.loaded;
  // }
  var postData = new FormData();
  for(key in s3Data.fields){
    postData.append(key, s3Data.fields[key]);
  }
  postData.append('file', file);

  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4){
      if(xhr.status === 200 || xhr.status === 204){

        return_field.value = filename;

      }
      else{

        alert("Could not upload file.");
      }
   }
  };
  xhr.send(postData);
}
s3_upload(doc_1, d1_filename, progress_doc_1);
s3_upload(doc_2, d2_filename, progress_doc_2);
s3_upload(doc_3, d3_filename, progress_doc_3);
s3_upload(doc_4, d4_filename, progress_doc_4);
s3_upload(doc_5, d5_filename, progress_doc_5);
