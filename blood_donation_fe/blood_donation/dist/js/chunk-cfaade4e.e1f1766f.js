(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-cfaade4e"],{"0a90":function(t,e,s){var n=s("63b6"),r=s("10ff");n(n.G+n.F*(parseFloat!=r),{parseFloat:r})},"10ff":function(t,e,s){var n=s("e53d").parseFloat,r=s("a1ce").trim;t.exports=1/n(s("e692")+"-0")!==-1/0?function(t){var e=r(String(t),3),s=n(e);return 0===s&&"-"==e.charAt(0)?-0:s}:n},"1d36":function(t,e,s){},"29e2":function(t,e,s){},"2da1":function(t,e,s){"use strict";var n=s("29e2"),r=s.n(n);r.a},"59ad":function(t,e,s){t.exports=s("7be7")},"78db":function(t,e,s){"use strict";var n=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col s12"},[s("div",{staticClass:"card padding-16 margin-4"},[s("div",{staticClass:"row zero-margin zero-padding valign-wrapper"},[s("div",{staticClass:"col s2 m2 l1"},[s("div",{staticClass:"circle teal valign-wrapper"},[s("span",{staticClass:"font-size-large white-text"},[t._v(t._s(t.bloodgroup))])])]),s("div",{staticClass:"col s10 m10 l11"},[""!=t.name?s("span",{staticClass:"font-size-large teal-text"},[t._v(t._s(t.name))]):t._e(),""!=t.name?s("br"):t._e(),""!=t.age?s("span",{staticClass:"font-size-small"},[t._v(t._s(t.age))]):t._e(),t._v(" \n        "),""!=t.gender?s("span",{staticClass:"font-size-small"},[t._v(t._s(t.gender))]):t._e(),""!=t.age&&""!=t.gender?s("br"):t._e(),"0"==t.where?s("span",{staticClass:"font-size-small"},[t._v(t._s(t.distance))]):t._e(),"0"==t.email?s("br"):t._e(),""!=t.email?s("span",{staticClass:"font-size-small"},[t._v(t._s(t.email))]):t._e()])]),t.isAuthorizedUserSearching&&"0"==t.where?s("div",{staticClass:"row zero-margin zero-padding center"},[""!=t.phonenumber?s("a",{staticClass:"waves-effect waves-light btn margin-top-16",attrs:{href:t.phonehref}},[t._v("Call")]):t._e(),t._v("\n       \n      "),s("a",{staticClass:"waves-effect waves-light btn margin-top-16",on:{click:t.requestForBloodDonation}},[t._v("Request Blood Donation")])]):t._e()])])},r=[],a=(s("7f7f"),{name:"SearchResult",created:function(){M.AutoInit()},props:["result","where"],computed:{isAuthorizedUserSearching:function(){try{return!!this.result.match_person}catch(t){return!1}},latitude:function(){try{return"Latitude: "+this.result.match_person.address_lat}catch(t){return this.result.latitude?"Latitude: "+this.result.latitude:"Latitude: "+this.result.address_lat}},latitudeVal:function(){try{return this.result.match_person.address_lat}catch(t){return this.result.latitude?this.result.latitude:this.result.address_lat}},longitude:function(){try{return"Longitude: "+this.result.match_person.address_long}catch(t){return this.result.longitude?"Longitude: "+this.result.longitude:"Longitude: "+this.result.address_long}},longitudeVal:function(){try{return this.result.match_person.address_long}catch(t){return this.result.longitude?this.result.longitude:this.result.address_long}},distance:function(){return"Distance (metres): "+this.result.distance_in_metres},name:function(){try{return this.result.match_person.name}catch(t){return this.result.name?this.result.name:""}},email:function(){try{return this.result.match_person.email}catch(t){return this.result.email?this.result.email:""}},age:function(){try{return"Age: "+this.result.match_person.age}catch(t){return""}},gender:function(){try{return"Gender: "+("M"===this.result.match_person.gender?"Male":"Female")}catch(t){return""}},bloodgroup:function(){try{return this.result.match_person.blood_group}catch(t){return this.result.blood_group}},phonenumber:function(){try{return"Phone: "+this.result.match_person.mobile_number}catch(t){return this.result.mobile_number?"Phone: "+this.result.mobile_number:""}},phonehref:function(){try{return"tel:"+this.result.match_person.mobile_number}catch(t){return""}}},methods:{requestForBloodDonation:function(){var t={search_match_donation_id:this.result.id};this.$store.dispatch("requestForBloodDonation",t).then(function(t){M.toast({html:t})})}}}),i=a,o=(s("2da1"),s("2877")),u=Object(o["a"])(i,n,r,!1,null,"30f4695d",null);e["a"]=u.exports},"7be7":function(t,e,s){s("0a90"),t.exports=s("584a").parseFloat},"7f7f":function(t,e,s){var n=s("86cc").f,r=Function.prototype,a=/^\s*function ([^ (]*)/,i="name";i in r||s("9e1e")&&n(r,i,{configurable:!0,get:function(){try{return(""+this).match(a)[1]}catch(t){return""}}})},a1ce:function(t,e,s){var n=s("63b6"),r=s("25eb"),a=s("294c"),i=s("e692"),o="["+i+"]",u="​",c=RegExp("^"+o+o+"*"),l=RegExp(o+o+"*$"),h=function(t,e,s){var r={},o=a(function(){return!!i[t]()||u[t]()!=u}),c=r[t]=o?e(d):i[t];s&&(r[s]=c),n(n.P+n.F*o,"String",r)},d=h.trim=function(t,e){return t=String(r(t)),1&e&&(t=t.replace(c,"")),2&e&&(t=t.replace(l,"")),t};t.exports=h},b676:function(t,e,s){"use strict";var n=s("1d36"),r=s.n(n);r.a},de7d:function(t,e,s){"use strict";s.r(e);var n,r=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"container relative requests-component-wrapper"},[t.loading?s("div",{staticClass:"progress preloader-wrapper"},[s("div",{staticClass:"indeterminate"})]):t._e(),t._m(0),0!=t.searchResults.length?s("div",{staticClass:"row"},t._l(t.searchResults,function(t){return s("SearchResult",{key:t.id,attrs:{result:t,where:"1"}})}),1):t._e()])},a=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"row center"},[s("br"),s("span",{staticClass:"font-size-large"},[t._v("Incoming Requests")])])}],i=s("bd86"),o=s("59ad"),u=s.n(o),c=(s("ac6a"),s("78db")),l=(n={name:"IncomingRequests",methods:{},created:function(){M.AutoInit()},data:function(){return{loading:!1,searchResults:[]}},components:{SearchResult:c["a"]}},Object(i["a"])(n,"methods",{}),Object(i["a"])(n,"mounted",function(){var t=this;this.$store.commit("setSearchMarkers",{newPoints:[]}),this.loading=!0,this.$store.dispatch("getReceivedRequests").then(function(e){t.searchResults=e;var s=[];t.searchResults.forEach(function(t){s.push({position:{lat:u()(t.address_lat),lng:u()(t.address_long)}})}),t.loading=!1,t.$store.commit("setSearchMarkers",{newPoints:s}),s.length>0&&t.$store.commit("setMapCenter",{mapCenter:{lat:s[0].position.lat,lng:s[0].position.lng}})})}),Object(i["a"])(n,"beforeRouteEnter",function(t,e,s){s(function(t){t.$store.commit("setIsIncomingRequestsOpen",!0)})}),Object(i["a"])(n,"beforeRouteLeave",function(t,e,s){s(),this.$store.commit("setIsIncomingRequestsOpen",!1)}),n),h=l,d=(s("b676"),s("2877")),m=Object(d["a"])(h,r,a,!1,null,"7be1363a",null);e["default"]=m.exports},e692:function(t,e){t.exports="\t\n\v\f\r   ᠎             　\u2028\u2029\ufeff"}}]);
//# sourceMappingURL=chunk-cfaade4e.e1f1766f.js.map