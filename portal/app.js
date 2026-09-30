const buttons = [...document.querySelectorAll("[data-filter]")];
const stages = [...document.querySelectorAll("#stages li")];
const result = document.querySelector("#filter-result");

function applyFilter(filter) {
  let visible = 0;
  for (const stage of stages) {
    const roles = stage.dataset.roles.split(" ");
    const show = filter === "all" || roles.includes(filter);
    stage.hidden = !show;
    if (show) visible += 1;
  }
  for (const button of buttons) {
    const selected = button.dataset.filter === filter;
    button.classList.toggle("active", selected);
    button.setAttribute("aria-pressed", String(selected));
  }
  result.textContent = `Mostrando ${visible} ${visible === 1 ? "etapa" : "etapas"}.`;
}

for (const button of buttons) {
  button.addEventListener("click", () => applyFilter(button.dataset.filter));
}

applyFilter("all");
