// Ambil elemen-elemen
let step = document.getElementsByClassName("step");
let prevBtn = document.getElementById("prev-btn");
let nextBtn = document.getElementById("next-btn");
let submitBtn = document.getElementById("submit-btn");
let form = document.getElementsByTagName("form")[0];
let succcessDiv = document.getElementById("success");

let current_step = 0;
let stepCount = step.length;

// Tampilkan langkah pertama
step[current_step].classList.add("d-block");
prevBtn.classList.add("d-none");
submitBtn.classList.add("d-none");
nextBtn.classList.add("d-inline-block");

// Tombol Next
nextBtn.addEventListener("click", () => {
  if (!validateStep(current_step)) return;

  step[current_step].classList.remove("d-block");
  step[current_step].classList.add("d-none");
  current_step++;

  step[current_step].classList.remove("d-none");
  step[current_step].classList.add("d-block");

  if (current_step > 0) prevBtn.classList.remove("d-none");
  if (current_step === stepCount - 1) {
    nextBtn.classList.add("d-none");
    submitBtn.classList.remove("d-none");
  }
  progress((100 / stepCount) * current_step);
});

// Tombol Previous
prevBtn.addEventListener("click", () => {
  if (current_step === 0) return;

  step[current_step].classList.remove("d-block");
  step[current_step].classList.add("d-none");
  current_step--;

  step[current_step].classList.remove("d-none");
  step[current_step].classList.add("d-block");

  if (current_step === 0) prevBtn.classList.add("d-none");
  nextBtn.classList.remove("d-none");
  submitBtn.classList.add("d-none");
  progress((100 / stepCount) * current_step);
});

// Tombol Submit
submitBtn.addEventListener("click", () => {
  if (!validateStep(current_step)) return;

  step[current_step].classList.remove("d-block");
  step[current_step].classList.add("d-none");

  prevBtn.classList.add("d-none");
  submitBtn.classList.add("d-none");

  succcessDiv.classList.remove("d-none");
  succcessDiv.classList.add("d-block");
  form.submit();
});

// Progress Bar
const progress = (value) => {
  const progressBar = document.querySelector(".progress-bar");
  if (progressBar) progressBar.style.width = `${value}%`;
};

// Validasi Step dengan SweetAlert2
function validateStep(stepIndex) {
  const inputs = step[stepIndex].querySelectorAll("input");
  for (const input of inputs) {
    const isRadio = input.type === "radio";
    const isNumber = input.type === "number";
    const isEmpty = input.value.trim() === "";
    const isUncheckedRadio =
      isRadio &&
      !step[stepIndex].querySelector(`input[name="${input.name}"]:checked`);

    if ((isRadio && isUncheckedRadio) || (isNumber && isEmpty)) {
      Swal.fire({
        icon: "info",
        title: "Oops!",
        text: "Harap isi atau pilih jawaban terlebih dahulu.",
        confirmButtonText: "Oke",
        confirmButtonColor: "#3085d6",
      });
      return false;
    }
  }
  return true;
}

// Jika form disubmit langsung
form.onsubmit = () => true;
