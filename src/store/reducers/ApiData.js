import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  SafeAreaView,
  ActivityIndicator,
} from "react-native";
import {
  SET_LOGIN_DATA,
  SET_LIST_DATA,
  SET_VERIFICATION_DATA,
  SET_ORDER_BOX_ID,
  CLEAR,
  SET_PO_NUMBER,
  CREATE_ORDER,
  SETEMAIL,
  UPDATEPROFILE,
  SETIMAGE,
  CLEAR_ALL,
  SET_LIST
} from "../actions/ApiData";
import AsyncStorage from "@react-native-community/async-storage";
import URL from "../../api/ApiURL";
const initialState = {
  ClientId: 0,
  Access: 0,
  Refresh: 0,
  ClientName: "",
  ClientEmail: "",
  ClientAddress: "",
  ClientPhoneNumber: "",
  ClientPackage: "",
  CompletedOrders: "",
  ProgressOrders: "",
  PendingOrders: "",
  RemainingInvoices: "",
  TotalInvoices: "",
  UsedInvoices: "",
  OrderId: "",
  PoNumber: "",
  ClientPhone: "",
  FirstName: "",
  LastName: "",
  ClientImage: "",
  RiderId:"",
  ProductList:[]
};

const ApiData = (state = initialState, action) => {
  switch (action.type) {
    case SETIMAGE:
      state.ClientImage = action.product;

      console.log("From Product listssssssss@@");
      return state;

      case SET_LIST:
        state.ProductList = action.product;
        return state;


    case UPDATEPROFILE:
      state.FirstName = action.firstname;
      state.LastName = action.lastname;

      state.ClientPhoneNumber = action.phoneNo;
      return state;

    case SETEMAIL:
      const newEmail = action.product;
      state.ClientEmail = newEmail;
      console.log(state.ClientEmail);
      return state;

    case SET_LOGIN_DATA:
      const My_Response = action.response;

      state.ClientId = My_Response.client_id;
      state.Access = My_Response.data.access;
      state.Refresh = My_Response.data.refresh;
     

      // console.log("Yesssssss")
      // fetch(URL+'/client_app/client_dashboard/'+state.ClientId+'/')
      // // fetch(URL+'/client_app/clients_list/33/')
      // .then((response) => response.json())
      // .then((responseJson) => {

      //     console.log("dashboard",responseJson)
      //     state.ClientName=responseJson.client.first_name+" "+responseJson.client.last_name;
      //     console.log("List: ",state.ClientName)
      //     state.ClientEmail=responseJson.client.email
      //     console.log("List: ",state.ClientEmail)
      //     state.ClientAddress=responseJson.client.address
      //     console.log("List: ",state.ClientAddress)
      //     state.ClientPhoneNumber=responseJson.client.phone_number
      //     console.log("List: ",state.ClientPhoneNumber)

      // //setListResponse(responseJson);
      // //check=false;
      // }) .catch ((error)=>
      // console.log("Something went wrong", error)
      // )

      //console.log("reducer",state.ClientId,state.Access,state.Refresh)
      return state;

    case SET_LIST_DATA:
      const ListResponse = action.response;

      console.log("reducerr", ListResponse);
      state.ClientName = ListResponse.client_dashboard.client_name;
      state.ClientPackage = ListResponse.client_dashboard.client_package;
      state.CompletedOrders =
        ListResponse.client_dashboard.no_of_completed_orders;
      state.ProgressOrders =
        ListResponse.client_dashboard.no_of_in_progress_orders;
      state.PendingOrders = ListResponse.client_dashboard.no_of_pending_orders;
      state.RemainingInvoices =
        ListResponse.client_dashboard.remaining_invoices;
      state.TotalInvoices = ListResponse.client_dashboard.total_invoices;
      state.UsedInvoices = ListResponse.client_dashboard.used_invoices;
      state.FirstName = ListResponse.client_dashboard.client_first_name;
      state.LastName = ListResponse.client_dashboard.client_last_name;
      state.ClientPhone = ListResponse.client_dashboard.client_phone;
      state.ClientEmail = ListResponse.client_dashboard.client_user_name;

      return state;

    case SET_ORDER_BOX_ID:
      const OrderId = action.response;
      // if(OrderId==1){
      //     state.OrderId="";
      // }
      // else{
      state.OrderId = OrderId;
      console.log("state.OrderId", state.OrderId);
      return state;

    // }
    //console.log("OrderID:",state.OrderId)

    case SET_PO_NUMBER:
      const po = action.product;
      state.PoNumber = po;

      return state;

      case CLEAR_ALL:
        const check = action.response;
        if (check == 1) {
          state.ClientId= 0,
          state.Access= 0,
          state.Refresh= 0,
          state.ClientName= "",
          state.ClientEmail= "",
          state.ClientAddress= "",
          state.ClientPhoneNumber= "",
          state.ClientPackage= "",
          state.CompletedOrders= "",
          state.ProgressOrders= "",
          state.PendingOrders= "",
          state.RemainingInvoices= "",
          state.TotalInvoices= "",
          state.UsedInvoices= "",
          state.OrderId="",
          state.PoNumber= "",
          state.ClientPhone= "",
          state.FirstName= "",
          state.LastName= "",
          state.ClientImage= "",
          state.RiderId=""
        
          // state.PoNumber="";
          console.log("clearrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", state.OrderId);
          // AsyncStorage.removeItem("OrderBoxId");
        }
  
        return state;

    case CLEAR:
      const checking = action.response;
      if (checking == 1) {
        state.OrderId = "";
        // state.PoNumber="";
        console.log("Updated state.orderId", state.OrderId);
        AsyncStorage.removeItem("OrderBoxId");
      }

      return state;

    case CREATE_ORDER:
      const checkCreate = action.product;
      if (checkCreate == 1) {
        console.log("Reducer Create");
        fetch(URL + "/order/create_order/", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            order_box: state.OrderId,
            purchase_order_no: state.PoNumber,
            order_title: "Grocery",
            delivery_person: 13,
            order_delivery_datetime: "2021-01-25",
            shipment_address: 1,
            delivery_notes: "note",
            comment: "note",
            distance: "2km",
            status: "Pending",
            payment_type: "cash_on_delivery",
          }),
        })
          .then(async (response) => {
            let data = await response.json();
            console.log("status code", response.status);
            // console.log("status code",data)
            if (response.status == 201) {
              console.log("Create response", data.order.order_products);
              alert("Thanks,Your Order is Placed,");
              // dispatch(ApiDataActions.SetLoginData(data));
              // navigation.navigate("MyDrawer");
            } else {
              alert("Unable to Create Order");
            }

            // code that can access both here
          })
          .catch((error) =>
            console.log("Something went wrong at create Order Box", error)
          );
      }

      return state;

    default:
      return state;
  }
};

export default ApiData;
