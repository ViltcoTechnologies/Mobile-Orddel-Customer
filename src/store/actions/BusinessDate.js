export const UPDATEBUISNESSDETAILS = "UPDATEBUISNESSDETAILS";
export const updateBuisnessDetail = (name, nature, type, address) => {
  console.log("from actionnnnnnnnnnnnnn", name, nature, type, address);

  return {
    type: UPDATEBUISNESSDETAILS,
    name: name,
    nature: nature,
    type: type,
    address: address,
  };
};
