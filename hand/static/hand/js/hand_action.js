const pre_btn = document.getElementById('go-to-pre')
pre_btn.addEventListener('click', e => {
   e.preventDefault();
   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.remove('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.add('d-none');
   });

   let turn = document.querySelectorAll('.turn-info');
   turn.forEach(upd => {
      upd.classList.add('d-none')
   });

   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.add('d-none')
   });

   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.add('active');

   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.remove('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.remove('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.remove('active');


})


const flop_btn = document.getElementById('go-to-flop')
flop_btn.addEventListener('click', e => {
   e.preventDefault();

   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.remove('d-none');
   });

   let turn = document.querySelectorAll('.turn-info');
   turn.forEach(upd => {
      upd.classList.add('d-none')
   });

   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.add('d-none')
   });
   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.remove('active');

   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.add('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.remove('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.remove('active');

})

const turn_btn = document.getElementById('go-to-turn')
turn_btn.addEventListener('click', e => {
   e.preventDefault()
   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.add('d-none');
   });

   let turn = document.querySelectorAll('.turn-info');
   turn.forEach(upd => {
      upd.classList.remove('d-none')
   });

   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.add('d-none')
   });

   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.remove('active');

   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.remove('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.add('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.remove('active');
})

const river_btn = document.getElementById('go-to-river');
river_btn.addEventListener('click', e => {
   e.preventDefault()
   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.add('d-none');
   });

   let turn = document.querySelectorAll('.turn-info')
   turn.forEach(upd => {
      upd.classList.add('d-none')
   });

   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.remove('d-none')
   });

   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.remove('active');
   
   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.remove('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.remove('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.add('active');

})

