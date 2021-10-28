<Autocomplete
                                autoCapitalize="none"
                                autoCorrect={false}
                                inputContainerStyle={{width:130}}
                                containerStyle={{backgroundColor: 'grey'}}
                                //data to show in suggestion
                                data={filteredProducts}
                                //default value if you want to set something in input
                                defaultValue={
                                JSON.stringify(selectedValue) === '{}' ? '' : selectedValue.name
                                }
                                /*onchange of the text changing the state of the query which will trigger
                                the findFilm method to show the suggestions*/
                                onChangeText={(text) => findName(text)}
                                placeholder="Add Item"
                                
                                //highlightTextColor="red"
                                renderItem={({item}) => (
                                //you can change the view you want to show in suggestion from here
                                <TouchableOpacity
                                style={{paddingHorizontal:10}}
                                    onPress={() => {
                                    setSelectedValue(item);
                                    setFilteredProducts([]);
                                    setUnitCheck(true);
                                    }}>
                                <Text style={styles.itemText}>{item.name} ({item.unit})</Text>
                                </TouchableOpacity>
                                )}
                    />