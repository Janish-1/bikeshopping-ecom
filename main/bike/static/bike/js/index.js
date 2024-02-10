const hamburer = document.querySelector(".hamburger");
const navList = document.querySelector(".nav-list");

if (hamburer) {
  hamburer.addEventListener("click", () => {
    navList.classList.toggle("open");
  });
}

// Popup
const popup = document.querySelector(".popup");
const closePopup = document.querySelector(".popup-close");

if (popup) {
  closePopup.addEventListener("click", () => {
    popup.classList.add("hide-popup");
  });

  window.addEventListener("load", () => {
    setTimeout(() => {
      popup.classList.remove("hide-popup");
    }, 1000);
  });
}
let cartIcon = document.querySelector("#cart-icon");

let cart = document.querySelector(".cart");
let closeCart = document.querySelector("#close-cart");

cartIcon.onclick = () => {
  cart.classList.add("active");
};
closeCart.onclick = () => {
  cart.classList.remove("active");
};

if (document.readyState == "loading") {
  document.addEventListener("DOMContentLoaded", ready);
} else {
  ready();
}

//Making Function
function ready(){
 var removeCartButtons =document.getElementsByClassName('cart-remove')
 console.log(removeCartButtons)
 for (var i=0;  i< removeCartButtons.length; i++){
   var button= removeCartButtons[i]
   button.addEventListener('click',removeCartItem)
 }
 //Quantiy Changes
 var quantityInputs = document.getElementsByClassName('cart-quantity')
 for (var i=0;  i< quantityInputs.length; i++){
   var input =quantityInputs[i]
   input.addEventListener('change',quantityChanged);

 }
 //Add to cart
 var addCart = document.getElementsByClassName('add-cart');
 for (var i=0;  i< addCart.length; i++){
   var button= addCart[i]
   button.addEventListener('click',addCartClicked)
 }
 //Buy button Work
 document.getElementsByClassName('btn-buy')[0].addEventListener('click',buyButtonClicked);
}

//Buy button 
function buyButtonClicked(){
  alert('Siparisiniz verilmistir... ')
  var cartContent =document.getElementsByClassName('cart-content')[0]
  while(cartContent.hasChildNodes()){
    cartContent.removeChild(cartContent.firstChild);
  }
updateTotal();
}


function removeCartItem(event){
  var buttonClicked = event.target
  buttonClicked.parentElement.remove()
  updateTotal();
}
//Add to cart
function addCartClicked(event){
  var button= event.target
  var shopProducts = button.parentElement
  var title =shopProducts.getElementsByClassName('product-title')[0].innerText;
   var price =
     shopProducts.getElementsByClassName("price")[0].innerText;
      var productImg =
        shopProducts.getElementsByClassName("product-img")[0].src;
       addProductToCart(title,price,productImg);
       updateTotal();

}
function addProductToCart(title,price,productImg){
  var cartShopBox = document.createElement('div')
  cartShopBox.classList.add('cart-box')
  var cartItems= document.getElementsByClassName('cart-content')[0];

  var cartItemNames =cartItems.getElementsByClassName('cart-product-title')
  for (var i=0;  i< cartItemNames.length; i++){
    if(cartItemNames[i].innerText==title){
    alert('Bu ürünü sepetinize zaten eklediniz');
    return;
     
    }

  }
var cartBoxContent = `<img src="${productImg}" alt="" class="cart-img">
                        <div class="detail-box">
                            <div class="cart-product-title">Earbuds</div>
                            <div class="cart-price">$25</div>
                            <input type="number" value="1" class="cart-quantity">
                        </div>
                        <!-- remove cart -->
                        <i class='bx bxs-trash-alt cart-remove' ></i>`;

cartShopBox.innerHTML = cartBoxContent;
cartItems.append(cartShopBox)
cartShopBox.getElementsByClassName('cart-remove')[0].addEventListener('click',removeCartItem)

cartShopBox
  .getElementsByClassName("cart-quantity")[0]
  .addEventListener("change", quantityChanged);



}
//Quantity Changes
function quantityChanged(event){
  var input = event.target
  if(isNaN(input.value) || input.value <= 0){
    input.value=1;
  }
  updateTotal();
}


//Update Total

function updateTotal(){
  var cartContent = document.getElementsByClassName('cart-content')[0]
  var  cartBoxes = cartContent.getElementsByClassName('cart-box')
  var total=0;
   for (var i=0;  i< cartBoxes.length; i++){

 var cartBox= cartBoxes[i];
 var priceElement= cartBox.getElementsByClassName('cart-price')[0];
 var quantityElement= cartBox.getElementsByClassName('cart-quantity')[0];
 var price =parseFloat(priceElement.innerText.replace("$", ""));
 var quantity= quantityElement.value;
 total=total +  (price * quantity);
   }
 total =Math.round(total *100) /100;



 document.getElementsByClassName('total-price')[0].innerText = '$' + total;

}










// prass


// var cartIcon = document.getElementById('cart-icon');
// var cart = document.getElementsByClassName('cart');
// var removeCart = document.getElementById('close-cart');

// //Open Cart
// cartIcon.addEventListener('click',()=>{
//     cart[0].classList.add('active');
// // });

// //Close Cart
// removeCart.addEventListener('click',()=>{
//     cart[0].classList.remove('active');
// });

// Cart working js

// t.readyState == "loading")
// {
//     document.addEventListener("DOMContentLoaded",ready);
// }
// else{
//     ready();
// }if(documen

// Making ready function

// function ready(){
      //Remove Items From Cart
    //   var removeCartButtons = document.getElementsByClassName('cart-remove');
    //   console.log(removeCartButtons);
    //   for(var i=0;i<removeCartButtons.length;i++)
    //   {
    //       var button = removeCartButtons[i];
    //       button.addEventListener('click',removeCartItems);
    //   }

      // Quantity Changes
    //   var quantityInputs = document.getElementsByClassName('cart-quantity');
    //   for(var i=0;i<quantityInputs.length;i++)
    //   {
    //       quantityInputs[i].addEventListener('change',quantityChanged);
    //   }

      // Add to cart
    //   var addCart = document.getElementsByClassName('add-cart');
    //   for(var i =0;i<addCart.length;i++)
    //   {
    //       var button = addCart[i];
    //       button.addEventListener('click',addCartClicked);
    //   }

      // Buy Button Working
    //   document.getElementsByClassName('btn-buy')[0].addEventListener('click',buyButtonClicked);
// }



// Buy Button Working 

// function buyButtonClicked()
// {   
  
//     var cartBox = document.getElementsByClassName('cart-box');
//     if(cartBox.length == 0)
//     {
//         alert("Your cart is Empty !!!");
//         return;
//     }
//     var cartContent = document.getElementsByClassName('cart-content')[0];
//     alert("Your order is placed !! Thank you for placing order");
//      while(cartContent.hasChildNodes())
//      {
//          cartContent.removeChild(cartContent.firstChild);
//      }

//      updateTotal();
// }



// Remove Items from Cart

// function removeCartItems(event){
//     var buttonClicked = event.target;
//     buttonClicked.parentElement.remove();
//     updateTotal();
// }

// Quantity Changed

// function quantityChanged(event){
//     var input = event.target;
//     if(isNaN(input.value) || input.value <= 0)
//     {
//         input.value = 1;
//     }

//     updateTotal();
// }

// Add to cart button clicked
// function addCartClicked(event){
//     var button = event.target;
//     var shopProducts = button.parentElement;
//     var title = shopProducts.getElementsByClassName('item-title')[0].innerText;
//     var price = shopProducts.getElementsByClassName('price')[0].innerText;
//     var productImg = shopProducts.getElementsByTagName('img')[0].src;
//     addProductToCart(title,price,productImg);
//     updateTotal();
// }


// Adding product to cart function

// function addProductToCart(title,price,productImg)
// {
//     var cartShopBox = document.createElement('div');
//     cartShopBox.classList.add('cart-box');
//     var cartItems = document.getElementsByClassName('cart-content')[0];
//     var cartItemsNames = cartItems.getElementsByClassName('cart-product-title');
//     var cartItemsPrice = cartItems.getElementsByClassName('cart-price');

//     for(var i=0;i<cartItemsNames.length;i++)
//     {   
//         if(cartItemsNames[i].innerText == title){
//             alert("You have already added this this item to cart");
//             return;
//         }
//     }


// var cartBoxContent = `<img src="${productImg}" alt="" class="cart-img">
//                         <div class="detail-box">
//                             <div class="cart-product-title">${title}</div>
//                             <div class="cart-price">${price}</div>
//                             <input type="number" value="1" class="cart-quantity">
//                             <!-- Remove Cart -->
//                         </div>
//                         <i class="bx bxs-trash-alt cart-remove"></i>`;

//     cartShopBox.innerHTML = cartBoxContent;
//     cartItems.append(cartShopBox);
//     cartShopBox.getElementsByClassName('cart-remove')[0]
//     .addEventListener('click',removeCartItems);
//     cartShopBox.getElementsByClassName('cart-quantity')[0]
//     .addEventListener('change',quantityChanged);
// }




//update total
// function updateTotal(){
//     var cartContent = document.getElementsByClassName("cart-content")[0];
//     var cartBoxes = cartContent.getElementsByClassName("cart-box");
//     var total = 0;

//     for(var i=0;i<cartBoxes.length;i++)
//     {   
//         var cartBox = cartBoxes[i];
//         var priceElement = cartBox.getElementsByClassName('cart-price')[0];
//         var quantityELement = cartBox.getElementsByClassName('cart-quantity')[0];
//         var quantity = quantityELement.value;
//         var price = parseFloat(priceElement.innerText.replace("$",""));
        // var price = parseFloat(priceElement.innerHTML.slice(1));
        // total = total + (price*quantity);
    // }
        // If price contains decimal part
        // total = Math.round(total*100)/100;
        // document.getElementsByClassName('total-price')[0].innerText = "$" + total;


// }

  // Sample data for image change
  const imageData = {
    alt: "Concepts Solid Pink Men’s Polo",
    src: "./images/product-5.jpg",
  };

  // Function to change the image when the link is clicked
  function changeImage() {
    // Get the image and link elements
    const productImage = document.getElementById("productImage");
    const productLink = document.getElementById("productLink");

    // Update the image source and alt text
    productImage.src = imageData.src;
    productImage.alt = imageData.alt;

    // Prevent the default link behavior (optional)
    event.preventDefault();
  }

  // Attach the click event to the link
  document.getElementById("productLink").addEventListener("click", changeImage);