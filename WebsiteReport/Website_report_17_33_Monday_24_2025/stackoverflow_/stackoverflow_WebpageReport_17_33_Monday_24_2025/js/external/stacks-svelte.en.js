"use strict";(self.webpackChunkstackoverflow=self.webpackChunkstackoverflow||[]).push([[8112],{11663:(s,e,t)=>{t.d(e,{E:()=>i});const i=s=>{const e=e=>{const t=e.target;s.contains(t)||s.dispatchEvent(new CustomEvent("outclick",{detail:t}))};return document.addEventListener("click",e,!0),{destroy(){document.removeEventListener("click",e,!0)}}}},51475:(s,e,t)=>{if(t.d(e,{E:()=>i.E,i:()=>d}),!/^((12|41)05|7150|9498)$/.test(t.j))var i=t(11663);var a=t(22024);const l=/^((120|410|697)5|7150|9498)$/.test(t.j)?null:["a[href]","area[href]",'input:not([disabled]):not([type="hidden"]):not([aria-hidden])',"select:not([disabled]):not([aria-hidden])","textarea:not([disabled]):not([aria-hidden])","button:not([disabled]):not([aria-hidden])","iframe","object","embed","[contenteditable]",'[tabindex]:not([tabindex^="-"])'],n=s=>{const e=document.defaultView?.getComputedStyle(s);return!(!e||"none"===e.getPropertyValue("display")||"hidden"===e.getPropertyValue("visibility"))},o=async s=>(await(0,a.io)(),[...s.querySelectorAll(l.join(", "))].filter(n)),r=s=>{s[0]&&s[0].focus()},c=s=>{s[s.length-1]&&s[s.length-1].focus()},d=(s,{active:e,initialFocusElement:t,returnFocusElement:i})=>{let a;const l=async e=>{const{key:t,shiftKey:i}=e;if("Tab"===t){e.preventDefault(),e.stopPropagation();const t=await o(s),a=document.activeElement;i?(({allFocusableItems:s,currentlyFocusedItem:e})=>{if(!e)return void c(s);const t=s.indexOf(e);if(0===t)return void c(s);const i=s[t-1];i&&i.focus()})({allFocusableItems:t,currentlyFocusedItem:a}):(({allFocusableItems:s,currentlyFocusedItem:e})=>{if(!e)return void r(s);const t=s.indexOf(e);if(s.length-1===t)return void r(s);const i=s[t+1];i&&i.focus()})({allFocusableItems:t,currentlyFocusedItem:a})}},n=async()=>{const e=await o(s);a??=document.activeElement,t?t.focus():r(e),document.addEventListener("keydown",l)},d=()=>{i?i.focus():a?.focus(),document.removeEventListener("keydown",l),a=null};return e&&n(),{update:({active:s})=>{s?n():d()},destroy:d}}},12166:(s,e,t)=>{t.d(e,{$n:()=>o,In:()=>a,N_:()=>r,aF:()=>C,AM:()=>J,qR:()=>E,hl:()=>F,hj:()=>K,EA:()=>u,y$:()=>d,ks:()=>Q});t(82170),t(76467);var i=t(58460);i.vsQ('<span><!> <span class="v-visible-sr"> </span></span>');function a(s,e){i.VCO(e,!1);const t=i.jsK();let a=i._w2(e,"src",8),l=i._w2(e,"title",8,""),n=i._w2(e,"native",8,!1),o=i._w2(e,"class",8,"");i.M3l((()=>(i.iTV(a()),i.iTV(l()),i.iTV(n()),i.iTV(o()))),(()=>{i.hZp(t,((s,e,t,i)=>{let a=s;return e&&(a=a.replace("</svg>","<title>"+e+"</title></svg>"),a=a.replace(' aria-hidden="true"',"")),t&&(a=a.replace(/class="/,'class="native ')),i&&(a=a.replace(/class="/,'class="'+i+" ")),a})(a(),l(),n(),o()))})),i.iqF();var r=i.Imx(),c=i.esp(r);i.qyt(c,(()=>i.JtY(t)),!1,!1),i.BCw(s,r),i.uYY()}i.vsQ('<img class="s-avatar--image" alt="" role="presentation">'),i.vsQ('<span class="s-avatar--letter" aria-hidden="true"> </span>'),i.vsQ('<!> <span class="v-visible-sr"> </span> <!>',1);var l=i.vsQ(' <span class="s-btn--badge"><span class="s-btn--number"><!></span></span>',1),n=i.vsQ("<!><!>",1);function o(s,e){const t=i.iWx(e),a=i.gjz(e,["children","$$slots","$$events","$$legacy"]),o=i.gjz(a,["branding","size","variant","weight","href","disabled","dropdown","icon","link","loading","selected","unset","class"]);i.VCO(e,!1);const r=i.jsK();let c=i._w2(e,"branding",8,""),d=i._w2(e,"size",8,""),v=i._w2(e,"variant",8,""),p=i._w2(e,"weight",8,""),u=i._w2(e,"href",8,void 0),f=i._w2(e,"disabled",8,!1),b=i._w2(e,"dropdown",8,!1),w=i._w2(e,"icon",8,!1),g=i._w2(e,"link",8,!1),m=i._w2(e,"loading",8,!1),_=i._w2(e,"selected",8,!1),h=i._w2(e,"unset",8,!1),y=i._w2(e,"class",8,"");i.M3l((()=>(i.iTV(y()),i.iTV(c()),i.iTV(d()),i.iTV(v()),i.iTV(p()),i.iTV(b()),i.iTV(g()),i.iTV(w()),i.iTV(h()),i.iTV(m()),i.iTV(_()))),(()=>{i.hZp(r,((s,e,t,i,a,l,n,o,r,c,d)=>{const v="s-btn";let p=v;return s&&(p+=" "+s),[e,t,i,a].forEach((s=>{s&&(p+=` ${v}__${s}`)})),l&&(p+=` ${v}__dropdown`),n&&(p+=` ${v}__link`),o&&(p+=` ${v}__icon`),r&&(p+=` ${v}__unset`),c&&(p+=" is-loading"),d&&(p+=" is-selected"),p})(y(),c(),d(),v(),p(),b(),g(),w(),h(),m(),_()))})),i.iqF();var $=i.Imx(),Q=i.esp($);i.ND4(Q,(()=>u()?"a":"button"),!1,((s,a)=>{let c;i.vNg((()=>c=i.vhI(s,c,{href:u(),class:i.JtY(r),disabled:!u()&&f()||null,"aria-disabled":u()&&f()?"true":null,...o},void 0,s.namespaceURI===i.pQb,s.nodeName.includes("-")))),i.f0J("click",s,(function(s){i.Ibr.call(this,e,s)}));var d=n(),v=i.esp(d);i.NIy(v,e,"default",{},null);var p=i.hg4(v),b=s=>{var t=l(),a=i.esp(t,!0);a.nodeValue=" ";var n=i.hg4(a),o=i.jfp(n),r=i.jfp(o);i.NIy(r,e,"badge",{},null),i.cLc(o),i.cLc(n),i.BCw(s,t)};i.if(p,(s=>{t.badge&&s(b)})),i.BCw(a,d)})),i.BCw(s,$),i.uYY()}i.vsQ('<div class="d-flex ai-center ps-relative w100"><textarea></textarea> <pre aria-hidden="true"> <br></pre></div>');function r(s,e){const t=i.gjz(e,["children","$$slots","$$events","$$legacy"]),a=i.gjz(t,["href","variant","disabled","dropdown","underlined","visited","class"]);i.VCO(e,!1);const l=i.jsK();let n=i._w2(e,"href",8,void 0),o=i._w2(e,"variant",8,""),r=i._w2(e,"disabled",8,!1),c=i._w2(e,"dropdown",8,!1),d=i._w2(e,"underlined",8,!1),v=i._w2(e,"visited",8,!1),p=i._w2(e,"class",8,"");i.M3l((()=>(i.iTV(p()),i.iTV(o()),i.iTV(c()),i.iTV(d()),i.iTV(v()))),(()=>{i.hZp(l,((s,e,t,i,a)=>{const l="s-link";let n=l;return s&&(n+=` ${s}`),e&&(n+=` ${l}__${e}`),t&&(n+=` ${l}__dropdown`),i&&(n+=` ${l}__underlined`),a&&(n+=` ${l}__visited`),n})(p(),o(),c(),d(),v()))})),i.iqF();var u=i.Imx(),f=i.esp(u);i.ND4(f,(()=>n()?"a":"button"),!1,((s,t)=>{let o;i.vNg((()=>o=i.vhI(s,o,{href:n(),class:i.JtY(l),disabled:!n()&&r()||null,"aria-disabled":n()&&r()?"true":null,...a},void 0,s.namespaceURI===i.pQb,s.nodeName.includes("-")))),i.f0J("click",s,(function(s){i.Ibr.call(this,e,s)}));var c=i.Imx(),d=i.esp(c);i.NIy(d,e,"default",{},null),i.BCw(t,c)})),i.BCw(s,u),i.uYY()}var c=i.vsQ('<div><div class="v-visible-sr"> </div></div>');function d(s,e){i.VCO(e,!1);const t=i.jsK();let a=i._w2(e,"label",8,"Loading…"),l=i._w2(e,"size",8,""),n=i._w2(e,"class",8,"");i.M3l((()=>(i.iTV(n()),i.iTV(l()))),(()=>{i.hZp(t,((s,e)=>{let t="s-spinner";return s&&(t+=" "+s),e&&(t+=" s-spinner__"+e),t})(n(),l()))})),i.iqF();var o=c(),r=i.jfp(o),d=i.jfp(r,!0);i.cLc(r),i.cLc(o),i.vNg((()=>{i.ysU(o,i.$z$(i.JtY(t))),i.jax(d,a())})),i.BCw(s,o),i.uYY()}var v=i.vsQ('<div class="d-flex g4 fd-column svelte-15wbbs5"><div class="s-skeleton bar-pill h16 w100 svelte-15wbbs5"></div> <div class="s-skeleton bar-pill h16 w80 svelte-15wbbs5"></div> <div class="s-skeleton bar-pill h16 w33 svelte-15wbbs5"></div> <span class="v-visible-sr svelte-15wbbs5"> </span></div>');const p={hash:"svelte-15wbbs5",code:'.s-skeleton.svelte-15wbbs5 {overflow:hidden;position:relative;}.s-skeleton.svelte-15wbbs5:after {opacity:25%;\n        animation: svelte-15wbbs5-flow 8s linear infinite;background-image:linear-gradient(\n            to right,\n            #ac76f0 8.33%,\n            #297fff 16.67%,\n            #6abcf8 25%,\n            #ac76f0 41.67%,\n            #297fff 58.34%,\n            #6abcf8 75.01%,\n            #ac76f0 83.34%\n        );background-size:400% 100%;content:"";inset:0;position:absolute;z-index:1;}\n\n    @keyframes svelte-15wbbs5-flow {\n        0% {\n            background-position: 400% 50%;\n        }\n        100% {\n            background-position: 0% 50%;\n        }\n    }'};function u(s,e){i.kZQ(s,p);let t=i._w2(e,"label",8,"Loading content...");var a=v(),l=i.hg4(i.jfp(a),6),n=i.jfp(l,!0);i.cLc(l),i.cLc(a),i.vNg((()=>i.jax(n,t()))),i.BCw(s,a)}var f=i.vsQ('<span class="s-label--status"><!></span>'),b=i.vsQ("<label><!><!></label>");if(4726==t.j)var w=t(54152);var g=i.vsQ('<p class="s-description mb0 mtn2"><!></p>'),m=i.vsQ('<div class="s-input-fill"><!></div>'),_=i.vsQ('<div class="s-input-icon"><!></div>'),h=i.vsQ('<div class="s-input-icon"><!></div>'),y=i.vsQ('<p class="s-input-message"><!></p>'),$=i.vsQ('<div class="d-flex fd-column gy4"><!> <!> <div class="d-flex"><!> <div class="ps-relative w100"><!> <input> <!></div></div> <!></div>');function Q(s,e){const t=i.iWx(e),l=i.gjz(e,["children","$$slots","$$events","$$legacy"]),n=i.gjz(l,["id","label","disabled","hideLabel","fillSide","name","optional","placeholder","readonly","required","size","state","type","class","i18nOptionalText","i18nRequiredText"]);i.VCO(e,!1);const o=i.jsK();let r=i._w2(e,"id",8),c=i._w2(e,"label",8),d=i._w2(e,"disabled",8,!1),v=i._w2(e,"hideLabel",8,!1),p=i._w2(e,"fillSide",8,"prepend"),u=i._w2(e,"name",8,void 0),Q=i._w2(e,"optional",8,!1),I=i._w2(e,"placeholder",8,""),T=i._w2(e,"readonly",8,!1),j=i._w2(e,"required",8,!1),L=i._w2(e,"size",8,""),C=i._w2(e,"state",8,""),x=i._w2(e,"type",8,"text"),Y=i._w2(e,"class",8,""),V=i._w2(e,"i18nOptionalText",8,void 0),k=i._w2(e,"i18nRequiredText",8,void 0);i.M3l((()=>(i.iTV(Y()),i.iTV(L()))),(()=>{i.hZp(o,((s,e)=>{const t="s-input";let i=t;return s&&(i+=" "+s),e&&(i+=` ${t}__${e}`),i})(Y(),L()))})),i.iqF();var N=$(),J=i.jfp(N);const z=i.Xdt((()=>v()?"v-visible-sr":""));!function(s,e){i.VCO(e,!1);const t=i.jsK();let a=i._w2(e,"id",8),l=i._w2(e,"size",8,""),n=i._w2(e,"optional",8,!1),o=i._w2(e,"required",8,!1),r=i._w2(e,"class",8,""),c=i._w2(e,"i18nOptionalText",8,"Optional"),d=i._w2(e,"i18nRequiredText",8,"Required");i.M3l((()=>(i.iTV(r()),i.iTV(l()))),(()=>{i.hZp(t,((s,e)=>{const t="s-label";let i=t;return s&&(i+=" "+s),e&&(i+=` ${t}__${e}`),i})(r(),l()))})),i.iqF();var v=b(),p=i.jfp(v);i.NIy(p,e,"default",{},null);var u=i.hg4(p),w=s=>{var e=f(),t=i.jfp(e),a=s=>{var e=i.Qq7();i.vNg((()=>i.jax(e,c()))),i.BCw(s,e)},l=s=>{var e=i.Qq7();i.vNg((()=>i.jax(e,d()))),i.BCw(s,e)};i.if(t,(s=>{n()?s(a):s(l,!1)})),i.cLc(e),i.vNg((()=>i.goL(e,"s-label--status__required",o()))),i.BCw(s,e)};i.if(u,(s=>{(n()||o())&&s(w)})),i.cLc(v),i.vNg((()=>{i.ysU(v,i.$z$(i.JtY(t))),i.aIK(v,"for",a())})),i.BCw(s,v),i.uYY()}(J,{get id(){return r()},get class(){return i.JtY(z)},get size(){return L()},get required(){return j()},get i18nRequiredText(){return k()},get optional(){return Q()},get i18nOptionalText(){return V()},children:(s,e)=>{i.K2T();var t=i.Qq7();i.vNg((()=>i.jax(t,c()))),i.BCw(s,t)},$$slots:{default:!0}});var K=i.hg4(J,2),B=s=>{var t=g(),a=i.jfp(t);i.NIy(a,e,"description",{},null),i.cLc(t),i.vNg((()=>i.aIK(t,"id",`${r()}-description`))),i.BCw(s,t)};i.if(K,(s=>{t.description&&s(B)}));var E=i.hg4(K,2),q=i.jfp(E),F=s=>{var t=m(),a=i.jfp(t);i.NIy(a,e,"fill",{},null),i.cLc(t),i.vNg((()=>{i.goL(t,"order-first","prepend"===p()),i.goL(t,"order-last","append"===p())})),i.BCw(s,t)};i.if(q,(s=>{t.fill&&s(F)}));var O=i.hg4(q,2),Z=i.jfp(O),P=s=>{var e=_(),t=i.jfp(e);const l=i.Xdt((()=>"credit-card"===x()?w.Bln:w.C0l));a(t,{get src(){return i.JtY(l)}}),i.cLc(e),i.vNg((()=>{i.goL(e,"s-input-icon__creditcard","credit-card"===x()),i.goL(e,"s-input-icon__search","search"===x())})),i.BCw(s,e)};i.if(Z,(s=>{"search"!==x()&&"credit-card"!==x()||s(P)}));var R=i.hg4(Z,2);let M;i.R0j(R);var U=i.hg4(R,2),D=s=>{var e=h(),t=i.jfp(e),l=s=>{a(s,{src:w.GBC})},n=s=>{var e=i.Imx(),t=i.esp(e),l=s=>{a(s,{src:w.VsF})},n=s=>{a(s,{src:w.O7Z})};i.if(t,(s=>{"success"===C()?s(l):s(n,!1)}),!0),i.BCw(s,e)};i.if(t,(s=>{"error"===C()?s(l):s(n,!1)})),i.cLc(e),i.BCw(s,e)};i.if(U,(s=>{C()&&s(D)})),i.cLc(O),i.cLc(E);var A=i.hg4(E,2),S=s=>{var t=y(),a=i.jfp(t);i.NIy(a,e,"message",{},null),i.cLc(t),i.vNg((()=>i.aIK(t,"id",`${r()}-message`))),i.BCw(s,t)};i.if(A,(s=>{t.message&&s(S)})),i.cLc(N),i.vNg((()=>{i.goL(N,"has-error","error"===C()),i.goL(N,"has-success","success"===C()),i.goL(N,"has-warning","warning"===C()),M=i.vhI(R,M,{id:r(),"aria-describedby":t.message?`${r()}-message`:t.description?`${r()}-description`:void 0,"aria-invalid":"error"===C(),class:i.JtY(o),type:"credit-card"===x()?"text":x(),disabled:d(),name:u(),placeholder:I(),readonly:T(),required:j(),...n}),i.goL(R,"s-input__creditcard","credit-card"===x()),i.goL(R,"s-input__search","search"===x()),i.goL(R,"blr0",t.fill&&"prepend"===p()),i.goL(R,"brr0",t.fill&&"append"===p())})),i.f0J("change",R,(function(s){i.Ibr.call(this,e,s)})),i.f0J("input",R,(function(s){i.Ibr.call(this,e,s)})),i.f0J("keydown",R,(function(s){i.Ibr.call(this,e,s)})),i.f0J("keyup",R,(function(s){i.Ibr.call(this,e,s)})),i.f0J("focus",R,(function(s){i.Ibr.call(this,e,s)})),i.f0J("blur",R,(function(s){i.Ibr.call(this,e,s)})),i.f0J("paste",R,(function(s){i.Ibr.call(this,e,s)})),i.BCw(s,N),i.uYY()}var I=t(22024);if(/^(1113|1888|3019|3231|4901|5878|6894|8264)$/.test(t.j))w=t(54152);var T=t(51475),j=i.vsQ('<div class="d-flex g8 s-modal--footer"><!></div>'),L=i.vsQ('<aside class="s-modal" role="dialog"><div role="document"><h1 class="s-modal--header"><!></h1> <div class="s-modal--body"><!></div> <!> <!></div></aside>');function C(s,e){const t=i.iWx(e);i.VCO(e,!1);const l=i.jsK();let n=i._w2(e,"id",8),r=i._w2(e,"visible",12,!1),c=i._w2(e,"state",8,""),d=i._w2(e,"class",8,""),v=i._w2(e,"i18nCloseButtonLabel",8,"Close"),p=i._w2(e,"preventCloseOnClickOutside",8,!1),u=i._w2(e,"hideCloseButton",8,!1);const f=(0,I.ur)(),b=()=>{r()&&(r(!1),f("close"))};i.M3l((()=>i.iTV(d())),(()=>{i.hZp(l,(s=>{let e="s-modal--dialog";return s&&(e+=" "+s),e})(d()))})),i.iqF(),i.TsN();var g=L();i.f0J("keydown",i.xa8,(s=>{"Escape"===s.key&&b()}));var m=i.jfp(g),_=i.jfp(m),h=i.jfp(_);i.NIy(h,e,"header",{},null),i.cLc(_);var y=i.hg4(_,2),$=i.jfp(y);i.NIy($,e,"body",{},null),i.cLc(y);var Q=i.hg4(y,2),C=s=>{var t=j(),a=i.jfp(t);i.NIy(a,e,"footer",{},null),i.cLc(t),i.BCw(s,t)};i.if(Q,(s=>{t.footer&&s(C)}));var x=i.hg4(Q,2),Y=s=>{o(s,{variant:"muted",icon:!0,get"aria-label"(){return v()},class:"s-modal--close",$$events:{click:b},children:(s,e)=>{a(s,{src:w.nFV,class:"modal-close"})},$$slots:{default:!0}})};i.if(x,(s=>{u()||s(Y)})),i.cLc(m),i.XId(m,(s=>(0,T.E)?.(s))),i.XId(m,((s,e)=>(0,T.i)?.(s,e)),(()=>({active:r()}))),i.QZP((()=>i.f0J("outclick",m,(()=>!p()&&b())))),i.cLc(g),i.vNg((()=>{i.aIK(g,"aria-hidden",!r()),i.aIK(g,"aria-labelledby",`${n()}-title`),i.aIK(g,"aria-describedby",`${n()}-description`),i.goL(g,"s-modal__danger","danger"===c()),i.goL(g,"s-modal__celebration","celebration"===c()),i.ysU(m,i.$z$(i.JtY(l))),i.aIK(_,"id",`${n()}-title`),i.aIK(y,"id",`${n()}-description`)})),i.BCw(s,g),i.uYY()}i.vsQ('<nav class="pl24"><ul class="list-reset s-pagination"><!></ul></nav>');i.vsQ('<li><a class="s-pagination--item"><!></a></li>');i.vsQ('<li class="s-pagination--item s-pagination--item__clear">…</li>');i.vsQ(' <span class="v-visible-sr"> </span>',1),i.vsQ('<span class="v-visible-sr"> </span> ',1),i.vsQ(' <span class="v-visible-sr"> </span>',1),i.vsQ("<!> <!> <!>",1);var x=t(12018);if(/^(47(26|33|68)|3433|5048|6894|7795)$/.test(t.j))var Y=t(52425);var V=t(7913);const k="popover-context";function N(s){let e=(0,I.SD)(k);if(void 0===e)throw new Error(`<${s} /> is missing a parent <Popover /> component.`);return e}function J(s,e){const t=i.gjz(e,["children","$$slots","$$events","$$legacy"]);i.VCO(e,!1);const[a,l]=i.DZI(),n=()=>i.Hzn(L,"$state",a),o=()=>i.Hzn(_,"$arrowEl",a),r=i.jsK();let c=i._w2(e,"id",8),d=i._w2(e,"autoshow",8,!1),v=i._w2(e,"visible",8,void 0),p=i._w2(e,"placement",8,"bottom"),u=i._w2(e,"strategy",8,"absolute"),f=i._w2(e,"trapFocus",8,!1),b=i._w2(e,"dismissible",8,!0),w=i._w2(e,"tooltip",8,!1);let g,m;const _=(0,x.T5)(),[h,y,$]=(0,V.K)({placement:p(),strategy:u(),middleware:[(0,Y.cY)(10),(0,Y.UU)(),(0,Y.mG)(),(0,V.U)({element:_})],onComputed({placement:s,middlewareData:e}){if(i.hYb(L,i.vzK(n).computedPlacement=s,i.vzK(n)),e.arrow&&o()){const{x:s,y:t}=e.arrow;Object.assign(o().style,{left:null!=s?`${s}px`:"",top:null!=t?`${t}px`:""})}}}),Q=(0,I.ur)(),T=(s=0)=>{window.clearTimeout(m),i.JtY(r)||n().visible||(m=window.setTimeout((()=>{i.hYb(L,i.vzK(n).visible=!0,i.vzK(n)),Q("open")}),s))},j=(s=0)=>{window.clearTimeout(m),i.JtY(r)||n().visible&&(m=window.setTimeout((()=>{i.hYb(L,i.vzK(n).visible=!1,i.vzK(n)),w()||g.focus(),Q("close")}),s))},L=(0,x.T5)({id:c(),controlled:void 0!==t.visible,visible:d(),dismissible:b(),trapFocus:f(),computedPlacement:p(),tooltip:w(),floatingRef:s=>{g=s,h(s)},floatingContent:y,arrowEl:_,onOutclick:s=>{b()&&s.detail!==g&&j()},open:T,openTooltip:()=>{w()&&T(300)},close:j,closeTooltip:()=>{w()&&j(100)},toggle:()=>{n().visible?j():T()}});(0,I.o)(k,L),i.M3l((()=>i.iTV(t)),(()=>{i.hZp(r,void 0!==t.visible)})),i.M3l((()=>(i.JtY(r),i.iTV(v()))),(()=>{i.JtY(r)&&i.hYb(L,i.vzK(n).visible=v(),i.vzK(n))})),i.M3l((()=>i.iTV(p())),(()=>{$({placement:p()})})),i.iqF(),i.TsN();var C=i.Imx();i.f0J("keydown",i.xa8,(s=>{"Escape"===s.key&&b()&&j()}));var N=i.esp(C);i.NIy(N,e,"default",{get visible(){return n().visible},open:T,close:j},null),i.BCw(s,C),i.uYY(),l()}var z=i.vsQ("<span><!></span>");function K(s,e){i.VCO(e,!1);const[t,a]=i.DZI(),l=()=>i.Hzn(c,"$state",t);let n=i._w2(e,"elementId",8,null),o=i.jsK(),r=i.jsK(),c=N("PopoverReference");(0,I.Rc)((()=>{i.hZp(r,((s,e,t)=>{const i=s?document.getElementById(s):e.firstElementChild;if(!i)throw new Error("No reference element found.");return t.floatingRef(i),i})(n(),i.JtY(o),l())),l().controlled||(l().tooltip?((s,e)=>{s.addEventListener("mouseenter",e.openTooltip),s.addEventListener("mouseleave",e.closeTooltip),s.addEventListener("focusin",e.openTooltip),s.addEventListener("focusout",e.closeTooltip),s.setAttribute("aria-describedby",`${e.id}-popover`)})(i.JtY(r),l()):((s,e)=>{if("button"!==s.tagName.toLowerCase()&&"button"!==s.role)throw new Error("Reference element must have a role of 'button' for uncontrolled popovers.");s.setAttribute("aria-controls",`${e.id}-popover`);const t=e.dismissible?e.toggle:e.open;s.addEventListener("click",t)})(i.JtY(r),l()))})),i.M3l((()=>(l(),i.JtY(r))),(()=>{l().controlled||l().tooltip||i.JtY(r)?.setAttribute("aria-expanded",Boolean(l().visible).toString())})),i.iqF(),i.TsN();var d=z(),v=i.jfp(d);i.NIy(v,e,"default",{},null),i.cLc(d),i.Lcc(d,(s=>i.hZp(o,s)),(()=>i.JtY(o))),i.BCw(s,d),i.uYY(),a()}if(/^(4733|5048)$/.test(t.j))w=t(54152);var B=i.vsQ('<button type="button"><!></button>');function E(s,e){i.VCO(e,!1);const[t,l]=i.DZI(),n=N("PopoverCloseButton");let o=i._w2(e,"label",8,"Close"),r=i._w2(e,"class",8,"");i.TsN();var c=B();a(i.jfp(c),{src:w.nFV}),i.cLc(c),i.vNg((()=>{i.aIK(c,"aria-label",o()),i.ysU(c,"s-popover--close s-btn s-btn__muted ps-absolute"+(r()?` ${r()}`:""))})),i.f0J("click",c,(function(...s){i.Hzn(n,"$state",t).close?.apply(this,s)})),i.f0J("click",c,(function(s){i.Ibr.call(this,e,s)})),i.BCw(s,c),i.uYY(),l()}var q=i.vsQ('<div><div class="s-popover--arrow"></div> <div class="s-popover--content p12 mn12"><div class="ps-relative"><!></div></div></div>');function F(s,e){i.VCO(e,!1);const[t,a]=i.DZI(),l=()=>i.Hzn(r,"$state",t);let n=i._w2(e,"role",8,null),o=i._w2(e,"class",8,""),r=N("PopoverContent"),c=i.jsK("s-popover");const d=l().arrowEl;l().tooltip&&i.hZp(c,i.JtY(c)+" s-popover__tooltip"),o()&&i.hZp(c,i.JtY(c)+" "+o()),i.TsN();var v=q(),p=i.jfp(v);i.Lcc(p,(s=>i.fTr(d,s)),(()=>i.Hzn(d,"$arrowEl",t)));var u=i.hg4(p,2),f=i.jfp(u),b=i.jfp(f);i.NIy(b,e,"default",{},null),i.cLc(f),i.cLc(u),i.cLc(v),i.XId(v,(s=>l().floatingContent?.(s))),i.XId(v,((s,e)=>(0,T.i)?.(s,e)),(()=>({active:l().trapFocus&&!!l().visible}))),i.XId(v,(s=>(0,T.E)?.(s))),i.QZP((()=>i.f0J("outclick",v,(function(...s){l().onOutclick?.apply(this,s)})))),i.QZP((()=>i.f0J("mouseenter",v,(function(...s){l().openTooltip?.apply(this,s)})))),i.QZP((()=>i.f0J("mouseleave",v,(function(...s){l().closeTooltip?.apply(this,s)})))),i.QZP((()=>i.f0J("focusin",v,(function(...s){l().openTooltip?.apply(this,s)})))),i.QZP((()=>i.f0J("focusout",v,(function(...s){l().closeTooltip?.apply(this,s)})))),i.vNg((()=>{i.aIK(v,"id",`${l().id}-popover`),i.ysU(v,`${i.JtY(c)}${l().visible?" is-visible":""}`),i.aIK(v,"role",n()||(l().tooltip?"tooltip":"dialog")),i.aIK(v,"data-popper-placement",l().computedPlacement)})),i.BCw(s,v),i.uYY(),a()}i.vsQ("<!> ",1),i.vsQ('<div class="s-post-summary--content-type"><!></div>');i.vsQ("<!> <!>",1),i.vsQ("<!> <!>",1),i.vsQ("<span><!></span>");i.vsQ('<span class="s-post-summary--stats-item-unit"> </span>'),i.vsQ('<div><span class="s-post-summary--stats-item-number"><!> </span> <!></div>');i.vsQ("<p> </p>");i.vsQ('<time class="s-user-card--time"> </time>'),i.vsQ('<div class="s-badge s-badge__xs s-badge__moderator">Mod</div>'),i.vsQ('<div class="s-badge s-badge__xs s-badge__staff">Staff</div>'),i.vsQ('<div class="s-badge s-badge__xs s-badge__admin">Admin</div>'),i.vsQ(" <!> <!> <!>",1),i.vsQ('<li class="s-user-card--rep"> </li>'),i.vsQ('<li class="s-award-bling s-award-bling__gold"> </li>'),i.vsQ('<li class="s-award-bling s-award-bling__silver"> </li>'),i.vsQ('<li class="s-award-bling s-award-bling__bronze"> </li>'),i.vsQ('<ul class="s-user-card--awards"><!> <!> <!> <!></ul>'),i.vsQ('<div class="s-user-card--role"> </div>'),i.vsQ('<div class="s-user-card--location"> </div>'),i.vsQ('<time class="s-user-card--time"> </time>'),i.vsQ('<div class="s-user-card--tags d-flex g4"><!></div>'),i.vsQ('<div class="s-user-card--type"><!></div>'),i.vsQ('<div><!> <!> <div class="s-user-card--info"><!> <!> <!> <!> <!> <!></div> <!></div>');i.vsQ('<div class="s-activity-indicator"><div class="v-visible-sr"> </div></div>'),i.vsQ("<!> ",1),i.vsQ('<div class="s-post-summary--meta-tags"><!></div>'),i.vsQ('<!> <span class="v-visible-sr"> </span>',1),i.vsQ("<!> <!>",1),i.vsQ('<div><div class="s-post-summary--stats"><!> <!> <!> <!> <!> <!></div> <div class="s-post-summary--content"><!> <h3 class="s-post-summary--content-title"><!> <!></h3> <!> <div class="s-post-summary--meta"><!> <!></div> <!> <!></div></div>');i.vsQ('<div class="s-post-summary--answer"><div class="s-post-summary--stats"><!> <!></div> <p class="s-post-summary--answer-excerpt"> </p> <div class="s-post-summary--meta"><!> <!></div></div>');i.vsQ('<p class="s-description mb0 mtn2"><!></p>'),i.vsQ('<div class="s-input-icon"><!></div>'),i.vsQ('<p class="s-input-message"><!></p>'),i.vsQ("<div><!> <!> <div><select><!></select> <!></div> <!></div>");i.vsQ("<option> </option>");i.vsQ('<span class="s-tag--sponsor"><!></span>'),i.vsQ('<button class="s-tag--dismiss" type="button"><span class="v-visible-sr"> </span><!></button>'),i.vsQ("<!> <!><!>",1)}}]);