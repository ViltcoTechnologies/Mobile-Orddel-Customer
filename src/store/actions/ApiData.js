export const SET_LOGIN_DATA = "SET_LOGIN_DATA";
export const SET_VERIFICATION_DATA = "SET_VERIFICATION_DATA";
export const SET_LIST_DATA = "SET_LIST_DATA";
export const SET_ORDER_BOX_ID = "SET_ORDER_BOX_ID";
export const ADD_TO_CART = "ADD_TO_CART";
export const CLEAR = "CLEAR";
export const SET_PO_NUMBER = "SET_PO_NUMBER";
export const CREATE_ORDER = "CREATE_ORDER";
export const SETEMAIL = "SETEMAIL";
export const UPDATEPROFILE = "UPDATEPROFILE";
export const SETIMAGE = "SETIMAGE";
export const CLEAR_ALL = "CLEAR_ALL";

export const SET_LIST = "SET_LIST";
export const SetLoginData = (res) => {
  return { type: SET_LOGIN_DATA, response: res };
};
export const SetVerificationData = (res) => {
  return { type: SET_VERIFICATION_DATA, response: res };
};
export const SetListData = (res) => {
  return { type: SET_LIST_DATA, response: res };
};
export const SetOrderBoxId = (res) => {
  return { type: SET_ORDER_BOX_ID, response: res };
};
export const Clear = (res) => {
  return { type: CLEAR, response: res };
};
export const Clear_All = (res) => {
  return { type: CLEAR_ALL, response: res };
};
export const addToCart = (product) => {
  return { type: ADD_TO_CART, product: product };
};
export const SetPoNumber = (product) => {
  return { type: SET_PO_NUMBER, product: product };
};
export const CreateOrder = (product) => {
  return { type: CREATE_ORDER, product: product };
};
export const SetEmail = (product) => {
  return { type: SETEMAIL, product: product };
};

export const SetList = (product) => {
  return { type: SET_LIST, product: product };
};

export const UpdateProfile = (firstname, lastname, phoneNo) => {
  return {
    type: UPDATEPROFILE,
    firstname: firstname,
    lastname: lastname,

    phoneNo: phoneNo,
  };
};
export const SetImage = (product) => {
  return { type: SETIMAGE, product: product };
};
