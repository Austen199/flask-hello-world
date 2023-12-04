    var fullName = document.getElementById('fullName');
    var userName = document.getElementById('username');
    var number = document.getElementById('Number');
    var email = document.getElementById('Email');
    var password = document.getElementById('Password');
    var confirmPassword = document.getElementById('ConfirmPassword');
    var text1 = document.getElementById('text1');


    let userDataMain = [];
    userDataMain = JSON.parse(localStorage.getItem("users")) || [];

function registerNow(){
    event.preventDefault();   
    if(fullName.value === '' || number.value === '' || email.value === '' || password.value === '' || confirmPassword.value === '') {
        Swal.fire({
            icon: "error",
            title: "required...",
            text: "please fill all fields carefully!",            
          });
    } else if (password.value !== confirmPassword.value) {
        Swal.fire({
            icon: "error",
            title: "password...",
            text: "Password & Confirm Password Mismatch!",            
          });
    }  else {
        const Toast = Swal.mixin({
            toast: true,
            position: "top-end",
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.onmouseenter = Swal.stopTimer;
              toast.onmouseleave = Swal.resumeTimer;
            }
          });
          Toast.fire({
            icon: "success",
            title: `${fullName.value} Registered successfully`
          });
    
    const checkUser = userDataMain.find((user) => {
      return user.email === email.value || user.userName === userName.value;      
    });

    if(checkUser) {
      return Swal.fire({
        icon: "error",
        title: "account...",
        text: "Account Already Exist!",            
      });

    }

          
    const user = {
        fullName : fullName.value,
        userName : userName.value,
        number : number.value,
        email : email.value,
        password : password.value,
        confirmPassword : confirmPassword.value
    };

    userDataMain.push(user);

    localStorage.setItem("users", JSON.stringify(userDataMain));

    

    setTimeout(() =>{
      window.location.replace('./signin.html');
      // window.location.href = './dashboard.html'
      
    },3000);

    
      

    
}

}


function getData(){
  var getUserData = document.querySelector('#getData');
  userDataMain = JSON.parse(localStorage.getItem("users"));
  getUserData.innerHTML = `
  <ul>
    <li>fullName: ${userDataMain[0].fullName} </li>
    <li>Email: ${userDataMain[0].email}</li>
    <li>userName: ${userDataMain[0].userName}</li>
    <li>number: ${userDataMain[0].number} </li>
  </ul>
  `
  
}


function redirectionsignup(){
  window.location.replace('./signin.html');
}

function redirectiontomainpage(){
  window.location.replace('./index.html');
  
}




function logOut() {  
  setTimeout(redirectionsignup, 1000);    
}




function login(){
  event.preventDefault();
  const email = document.getElementById('Email').value;
  const password = document.getElementById('Password').value;
  userDataMain = JSON.parse(localStorage.getItem("users")) || [];
 

  if(userDataMain.length === 0){
    Swal.fire({
      icon: "error",
      title: "No users found",
      text: "Please sign up before logging in!",
    });
    return;
  }

  let user = userDataMain.find((user) => user.email === email);

  if(!user){
    Swal.fire({
      icon: "error",
      title: "User not found",
      text: "Email or Password is invalid!",
    });
    return;
  } 
  
  if(user.password !== password){
    Swal.fire({
      icon: "error",
      title: "Password mismatch",
      text: "Email or Password is invalid!",
    });
    return;
  }


  

//   if(!userDataMain){
//     console.log(!userDataMain);
//     return window.location.href = './signin.html'
//   } else if (userDataMain.email !== email.value || userDataMain.password !== password.value){
//   Swal.fire({
//     icon: "error",
//     title: "email & password...",
//     text: "email or Password Invalid or Mismatch!",            
//   });
// } 

  const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.onmouseenter = Swal.stopTimer;
      toast.onmouseleave = Swal.resumeTimer;
    }
  });
  Toast.fire({
    icon: "success",
    title: `${email} login successfully`
  });

setTimeout(() =>{
  window.location.replace('./dashboard.html'); 
  },4000);

}

function password_show_hide() {
  var x = document.getElementById("Password");
  var show_eye = document.getElementById("show_eye");
  var hide_eye = document.getElementById("hide_eye");
  hide_eye.classList.remove("d-none");
  if (x.type === "password") {
    x.type = "text";
    show_eye.style.display = "none";
    hide_eye.style.display = "block";
  } else {
    x.type = "password";
    show_eye.style.display = "block";
    hide_eye.style.display = "none";
  }
}


function password_show_hide1() {
  var xx = document.getElementById("ConfirmPassword");
  var show_eye = document.getElementById("show_eyee");
  var hide_eye = document.getElementById("hide_eyee");
  hide_eye.classList.remove("d-none");
  if (xx.type === "Password") {
    xx.type = "text";
    show_eye.style.display = "none";
    hide_eye.style.display = "block";
  } else {
    xx.type = "password";
    show_eye.style.display = "block";
    hide_eye.style.display = "none";
  }
}