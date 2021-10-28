export const ADD_TO_CART = 'ADD_TO_CART';
export const REMOVE_FROM_CART = 'REMOVE_FROM_CART';
export const ALL_CLEAR = 'ALL_CLEAR';
export const DELETE_PRODUCT = 'DELETE_PRODUCT';
export const ADD_TO_QTTY = 'ADD_TO_QTTY';
export const REORDER = 'REORDER';
export const RESEND = 'RESEND';
export const UPDATE_QTTY = 'UPDATE_QTTY';
export const UPDATE_TOTAL = 'UPDATE_TOTAL';


export const addToCart = (product,qtty) => {
  return { type: ADD_TO_CART, product: product,qtty:qtty };
};

export const removeFromCart = (mealId) => {
  return { type: REMOVE_FROM_CART, pid: mealId };
};

export const allClear = clear => {
  return { type: ALL_CLEAR, pid: clear };
};

export const deleteProduct = id => {
  return { type: DELETE_PRODUCT, pid: id };
};
export const addToQtty = (id) => {
  return { type: ADD_TO_QTTY, pid: id };
};

export const reorder = (data) => {
  return { type: REORDER, response: data };
};

export const resend = (data) => {
  return { type: RESEND, response: data };
};

export const updateQtty = (id,qtty) => {
  return { type: UPDATE_QTTY, id:id,qtty:qtty };
};

export const updateTotal = (id,qtty) => {
  return { type: UPDATE_TOTAL, id:id,qtty:qtty };
};