"use strict";(self.webpackChunkstackoverflow=self.webpackChunkstackoverflow||[]).push([[3773],{1845:(e,t,n)=>{n(86671),n(453);StackExchange=window.StackExchange=window.StackExchange||{},StackOverflow=window.StackOverflow=window.StackOverflow||{};n(52945)},1329:(e,t,n)=>{n.d(t,{C:()=>f});var o=n(94823),a=n(86671),c=n(29604);function r(e){$(e.target).text("Joined"),$(e.target).removeClass("s-btn__danger s-btn__filled ba bc-white")}function i(e){$(e.target).text("Leave"),$(e.target).addClass("s-btn__danger s-btn__filled ba bc-white")}function s(e){if(e.preventDefault(),c.A.user.isAnonymous)dispatchEvent(new CustomEvent("signupModalShow",{detail:{location:"anon_collective_public_discussions"}}));else{var t=$(e.target).prop("formAction");$.ajax({type:"post",url:t,data:{fkey:c.A.user.fkey,referrerUrl:document.URL}}).done(o.iY).fail((function(){(0,a.P0)("An error occurred.",{type:"danger"})}))}}function f(e=!1){const t=$(".js-leave-community"),n=$(".js-join-leave-container").find("form"),o=".membership";e||(t.off("mouseleave"+o).on("mouseleave"+o,r),t.off("mouseenter"+o).on("mouseenter"+o,i)),n.find(":input[formaction]").off("click"+o).on("click"+o,s)}}}]);