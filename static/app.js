$(".new-word").on("click",function(e){
    e.preventDefault()
    console.log("YES")
})

$(".taggle").on("click",()=>{
    $(".modal-body").toggle()
})