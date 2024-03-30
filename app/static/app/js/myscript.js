
$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var quan=this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/plus",
        data:{
            prod_id:id
        },
        success:function(data){
            quan.innerHTML=data.quantity,
            document.getElementById("amount").innerHTML=data.amount,
            document.getElementById("shipping_amount").innerHTML=data.shipping_amount,
            document.getElementById("totalamount").innerHTML=data.totalamount
        },
        error:function(data){
            console.log("data")
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var quan=this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/minus",
        data:{
            prod_id:id
        },
        success:function(data){
            quan.innerHTML=data.quantity,
            document.getElementById("amount").innerHTML=data.amount,
            document.getElementById("shipping_amount").innerHTML=data.shipping_amount,
            document.getElementById("totalamount").innerHTML=data.totalamount
        },
        error:function(data){
            console.log("data")
        }
    })
})

$('.remove').click(function(){
    var id=$(this).attr("pid").toString();
    var item=this
    $.ajax({
        type:"GET",
        url:"/remove",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("amount").innerHTML=data.amount,
            document.getElementById("shipping_amount").innerHTML=data.shipping_amount,
            document.getElementById("totalamount").innerHTML=data.totalamount,
            item.parentNode.parentNode.parentNode.parentNode.remove()
        },
        error:function(data){
            console.log(data)
        }
    })
})

$('#plus-buy-now').click(function(){
    var id=$(this).attr("pid").toString();
    var quan=document.getElementById("buy-quantity").innerHTML
    $.ajax({
        type:"GET",
        url:"/plus-buy-now",
        data:{
            prod_id:id,
            quantity:quan
        },
        success:function(data){
            document.getElementById("buy-quantity").innerHTML=data.quantity,
            document.getElementById("buy-amount").innerHTML=data.amount,
            document.getElementById("buy-shipping_amount").innerHTML=data.shipping_amount,
            document.getElementById("buy-totalamount").innerHTML=data.totalamount
        },
        error:function(data){
            console.log("data")
        }
    })
})

$('#minus-buy-now').click(function(){
    var id=$(this).attr("pid").toString();
    var quan=document.getElementById("buy-quantity").innerHTML
    $.ajax({
        type:"GET",
        url:"/minus-buy-now",
        data:{
            prod_id:id,
            quantity:quan
        },
        success:function(data){
            document.getElementById("buy-quantity").innerHTML=data.quantity,
            document.getElementById("buy-amount").innerHTML=data.amount,
            document.getElementById("buy-shipping_amount").innerHTML=data.shipping_amount,
            document.getElementById("buy-totalamount").innerHTML=data.totalamount
        },
        error:function(data){
            console.log("data")
        }
    })
})

function data() {
    q = document.getElementById("buy-quantity").innerHTML
    document.getElementById("quan").value = q
    a = document.getElementById("buy-totalamount").innerHTML
    document.getElementById("tamount").value = a
}