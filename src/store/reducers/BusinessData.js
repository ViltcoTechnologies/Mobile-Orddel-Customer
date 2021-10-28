import { UPDATEBUISNESSDETAILS } from "../actions/BusinessDate";
const initialState = {
  BuisnessName: "",
  BuisnessType: "",
  BuisnessNature: "",
  BuisnessAddress: "",
};

const BusinessData = (state = initialState, action) => {
  switch (action.type) {
    case UPDATEBUISNESSDETAILS:
      console.log(
        "from reducer----------------------------------------------------------------"
      );
      state.BuisnessName = action.name;
      state.BuisnessNature = action.nature;
      state.BuisnessType = action.type;
      state.BuisnessAddress = action.address;
      console.log(
        state.BuisnessName,
        "----------------------Buisness NAme --==="
      );

      return state;
    default:
      return state;
  }
};

export default BusinessData;
