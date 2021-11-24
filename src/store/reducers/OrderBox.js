import React, { useState } from "react";
import {
  ADD_TO_CART,
  REMOVE_FROM_CART,
  UPDATE_TOTAL,
  ALL_CLEAR,
  DELETE_PRODUCT,
  ADD_TO_QTTY,
  REORDER,
  RESEND,
  UPDATE_QTTY,
} from "../actions/OrderBox";
import ProductItem from "../../Models/Product";

const initialState = {
  totalPackages: 0,
  count: 0,
  totalAmount: 0,
  cardItemsArray: [],
};

export default (state = initialState, action) => {
  switch (action.type) {
    case UPDATE_TOTAL:
      console.log("UPDATE_QTTY id ", action.id);
      // console.log("UPDATE_QTTY Qty--------- ",state.cardItemsArray[action.id]["quantity"]);
      // console.log("UPDATE_QTTY items ",state.items);

      console.log("UPDATE_QTTY  ", state.count);
      // const [qtyCheck,setQtyCheck]=useState(false);
      // const [newQty,setNewQty]=useState("");
      // var qtyCheck=false;
      // var Qty=0;
      var newQuantity2 = action.qtty;

      var FindItem2 = state.cardItemsArray.find(
        (item) => item.id === action.id
      );
      // state.totalPackages=parseInt(state.totalPackages) - parseInt(FindItem.quantity);
      // state.totalPackages=parseInt(state.totalPackages) + parseInt(action.qtty);
      var objIndex2 = state.cardItemsArray.findIndex(
        (obj) => obj.id == action.id
      );
      // state.cardItemsArray[objIndex].quantity = newQuantity;
      state.totalAmount = 0;
      for (var j = 0; j < state.cardItemsArray.length; j++) {
        state.totalAmount =
          state.totalAmount + state.cardItemsArray[j].total_amount;
      }

      // if (state.totalAmount > state.cardItemsArray[objIndex2].total_amount) {
      //   state.totalAmount =
      //     parseFloat(state.totalAmount) -
      //     parseFloat(state.cardItemsArray[objIndex2].total_amount);
      //   console.log("state.totalAmount 1 ", state.totalAmount);
      // } else {
      //   state.totalAmount =
      //     parseFloat(state.cardItemsArray[objIndex2].total_amount) -
      //     parseFloat(state.totalAmount);
      //   console.log("state.totalAmount 2 ", state.totalAmount);
      // }
      // state.totalAmount =
      //   parseFloat(state.totalAmount) +
      //   parseInt(newQuantity2) *
      //     parseFloat(state.cardItemsArray[objIndex2].price);
      // console.log("state.totalAmount 3 ", state.totalAmount);

      return {
        ...state,
        // items: state.items,
        totalPackages: state.totalPackages,
        count: state.count,
        totalAmount: state.totalAmount,
        cardItemsArray: state.cardItemsArray,
      };

    case UPDATE_QTTY:
      console.log("UPDATE_QTTY id ", action.id);
      // console.log("UPDATE_QTTY Qty--------- ",state.cardItemsArray[action.id]["quantity"]);
      // console.log("UPDATE_QTTY items ",state.items);

      console.log("UPDATE_QTTY  ", state.count);
      // const [qtyCheck,setQtyCheck]=useState(false);
      // const [newQty,setNewQty]=useState("");
      var qtyCheck = false;
      var Qty = 0;
      var newQuantity = action.qtty;

      var FindItem = state.cardItemsArray.find((item) => item.id === action.id);
      state.totalPackages =
        parseInt(state.totalPackages) - parseInt(FindItem.quantity);
      state.totalPackages =
        parseInt(state.totalPackages) + parseInt(action.qtty);
      var objIndex = state.cardItemsArray.findIndex(
        (obj) => obj.id == action.id
      );
      state.cardItemsArray[objIndex].quantity = newQuantity;
      state.cardItemsArray[objIndex].total_amount =
        newQuantity * state.cardItemsArray[objIndex].price;
      state.totalAmount = 0;
      for (var j = 0; j < state.cardItemsArray.length; j++) {
        state.totalAmount =
          state.totalAmount + state.cardItemsArray[j].total_amount;
      }
      console.log("@@@@@@@@@@@@     .......", state.cardItemsArray);
      // state.cardItemsArray[objIndex].total_amount =
      //   newQuantity * state.cardItemsArray[objIndex].price;

      // if (state.totalAmount > state.cardItemsArray[objIndex].total_amount) {
      //   console.log("state.totalAmount 1 ", state.totalAmount);
      //   state.totalAmount =
      //     parseFloat(state.totalAmount) -
      //     parseFloat(state.cardItemsArray[objIndex].total_amount);
      // } else {
      //   console.log("state.totalAmount 2 ", state.totalAmount);
      //   state.totalAmount =
      //     parseFloat(state.cardItemsArray[objIndex].total_amount) -
      //     parseFloat(state.totalAmount);
      // }
      // state.totalAmount =
      //   parseFloat(state.totalAmount) +
      //   parseInt(newQuantity) *
      //     parseFloat(state.cardItemsArray[objIndex].price);
      // console.log("state.totalAmount 3 ", state.totalAmount);

      // state.totalAmount=parseFloat(state.totalAmount)- parseFloat(FindItem.quantity*FindItem.price);
      // state.totalAmount=parseFloat(state.totalAmount)+ parseFloat(state.cardItemsArray[objIndex].quantity*state.cardItemsArray[objIndex].price);

      // state.cardItemsArray[action.id]["quantity"]=newQuantity;

      // if(state.totalAmount>state.cardItemsArray[objIndex].total_amount){
      //   console.log("state.totalAmount 1 ",state.totalAmount);
      //   state.totalAmount=parseFloat(state.totalAmount)- parseFloat(state.cardItemsArray[objIndex].total_amount);
      // }
      // else{
      //   console.log("state.totalAmount 2 ",state.totalAmount);
      //   state.totalAmount=parseFloat(state.cardItemsArray[objIndex].total_amount)-parseFloat(state.totalAmount);
      // }
      // state.totalAmount=parseFloat(state.totalAmount)+ parseInt(newQuantity)*parseFloat(state.cardItemsArray[objIndex].price);
      //     console.log("state.totalAmount 3 ",state.totalAmount)

      return {
        ...state,
        // items: state.items,
        totalPackages: state.totalPackages,
        count: state.count,
        totalAmount: state.totalAmount,
        cardItemsArray: state.cardItemsArray,
      };

    case RESEND:
      const Data = action.response;
      console.log("dataaaaaaaaaaa ====RESEND======>>>>", Data);
      // for (let i = 0; i < Data.length; i++) {
      //
      //   let updatedOrListCartItem1;
      //
      //   //updatedOrListCartItem1 = new ProductItem(Data[i]["quantity"],Data[i]["quantity"]*Data[i]["unit_sales_price"],Data[i]["product_name"],Data[i]["product_unit"],Data[i]["unit_sales_price"] );
      //   updatedOrListCartItem1 = new ProductItem(
      //     Data[i]["quantity"],
      //     Data[i]["quantity"] * Data[i]["avg_price"],
      //     Data[i]["product_name"],
      //     Data[i]["product_unit"],
      //     Data[i]["avg_price"]
      //   );
      //   (state.cardItemsArray = [
      //     { id: Data[i]["product_id"], ...updatedOrListCartItem1 },
      //     ...state.cardItemsArray,
      //   ]),
      //     // state.items={ ...state.items, [Data[i]["product_id"]]: updatedOrListCartItem1 }
      //     (state.totalPackages =
      //       parseInt(state.totalPackages) + parseInt(Data[i]["quantity"]));
      //   state.count = state.count + 1;
      //   state.totalAmount =
      //     parseFloat(state.totalAmount) +
      //     parseFloat(Data[i]["quantity"] * Data[i]["avg_price"]);
      //   console.log("state.cardItemsArray ======>>>>>>",state.cardItemsArray);
      // }

        let tempArray = [];
        Data.map((item)=>{
          tempArray.push(
                {
                  id:item.product_id,
                  name:item.product_name,
                  price:parseFloat(item.avg_price),
                  quantity:item.quantity,
                  total_amount:parseFloat(item.quantity * item.avg_price),
                  unit:item.product_unit
                }
            );
          state.totalAmount =parseFloat(state.totalAmount) +  parseFloat(item.quantity * item.avg_price);
          state.totalPackages = parseInt(state.totalPackages) + parseInt(item.quantity);

        });



        state.cardItemsArray = tempArray;


      return state;

    case REORDER:
      const data = action.response;
      // console.log("dataaaaaaaaaaa", data);
      // for (var i = 0; i < data.length; i++) {
      //   let updatedOrListCartItem;
      //
      //   updatedOrListCartItem = new ProductItem(
      //     data[i]["purchased_quantity"],
      //     data[i]["purchased_quantity"] * data[i]["avg_price"],
      //     data[i]["product_name"],
      //     data[i]["product_unit"],
      //     data[i]["avg_price"]
      //   );
      //   (state.cardItemsArray = [
      //     { id: data[i]["product_id"], ...updatedOrListCartItem },
      //     ...state.cardItemsArray,
      //   ]),
      //     // state.items={ ...state.items, [data[i]["product_id"]]: updatedOrListCartItem }
      //     (state.totalPackages =
      //       parseInt(state.totalPackages) +
      //       parseInt(data[i]["purchased_quantity"]));
      //   state.count = state.count + 1;
      //   state.totalAmount =
      //     parseFloat(state.totalAmount) +
      //     parseFloat(data[i]["purchased_quantity"] * data[i]["avg_price"]);
      // }
      // return state;

      let temp = [];
      data.map((item)=>{
        console.log("item in Redux ====>>>",item)
        temp.push(
            {
              id:item.product_id,
              name:item.product_name,
              price:parseFloat(item.avg_price),
              quantity:item.quantity,
              total_amount:parseFloat(item.quantity * item.avg_price),
              unit:item.product_unit
            }
        );
        state.totalAmount = parseFloat(state.totalAmount) + parseFloat(item.purchased_quantity * item.avg_price);
        state.totalPackages = parseInt(state.totalPackages) + parseInt(item.quantity);
      });

      state.cardItemsArray = temp;


      return state;

    case ADD_TO_CART:
      const addedProduct = action.product;
      const qtty = action.qtty;
      const id = addedProduct.id;
      const prodPrice = addedProduct.avg_price;
      const prodName = addedProduct.name;
      const prodUnit = addedProduct.unit;
      console.log("addedProduct", addedProduct.id);
      let updatedOrNewCartItem;

      updatedOrNewCartItem = new ProductItem(
        qtty,
        qtty * prodPrice,
        prodName,
        prodUnit,
        prodPrice
      );

      return {
        ...state,
        cardItemsArray: [
          { id: addedProduct.id, ...updatedOrNewCartItem },
          ...state.cardItemsArray,
        ],
        // items: { ...state.items, [addedProduct.id]: updatedOrNewCartItem },
        totalPackages: parseInt(state.totalPackages) + parseInt(qtty),
        count: state.count + 1,
        totalAmount:
          parseFloat(state.totalAmount) + parseFloat(qtty * prodPrice),
      };

    // case REMOVE_FROM_CART:
    //   var selectedCartItem = state.items[action.pid];
    //   var currentQty = selectedCartItem.quantity;
    //   let updatedCartItems;
    //   if (currentQty > 1) {
    //     // need to reduce it, not erase it
    //     const updatedCartItem = new ProductItem(
    //       selectedCartItem.quantity - 1,
    //       selectedCartItem.totalPackages - selectedCartItem.price,
    //       selectedCartItem.name,
    //       selectedCartItem.unit,
    //       selectedCartItem.price,

    //     );
    //     updatedCartItems = { ...state.items, [action.pid]: updatedCartItem };
    //   } else {
    //     updatedCartItems = { ...state.items };
    //     delete updatedCartItems[action.pid];
    //   }
    //   return {
    //     ...state,
    //     items: updatedCartItems,
    //     totalPackages: state.totalPackages - selectedCartItem.price,
    //     count: state.count-1,
    //   };
    // case ADD_ORDER:
    //   return initialState;
    case DELETE_PRODUCT:
      var item = state.cardItemsArray.find((item) => item.id === action.pid);
      // console.log("Garliccc",item);
      // if (!state.cardItemsArray[item]) {
      //   return state;
      // }
      const removeIndex = state.cardItemsArray
        .map(function (item) {
          return item.id;
        })
        .indexOf(action.pid);
      state.cardItemsArray.splice(removeIndex, 1);
      // console.log("state.cardItemsArray",state.cardItemsArray);
      // const updatedItems =  {...state.cardItemsArray} ;
      // const itemQty = state.cardItemsArray[action.pid].quantity;
      // const itemTotal=state.cardItemsArray[action.pid].price;
      // delete updatedItems[item];
      return {
        ...state,
        cardItemsArray: state.cardItemsArray,
        totalPackages: state.totalPackages - item.quantity,
        count: state.count - 1,
        totalAmount:
          state.cardItemsArray == ""
            ? 0
            : parseFloat(state.totalAmount) -
              parseFloat(item.quantity * item.price),
      };

    case ALL_CLEAR:
      if (action.pid == 1) {
        state.cardItemsArray = [];
        state.totalPackages = 0;
        state.count = 0;
        state.totalAmount = 0;
      }
  }

  return state;
};
