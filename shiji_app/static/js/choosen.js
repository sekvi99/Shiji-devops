const dashboard = document.getElementById('dashboardLink');
const about = document.getElementById('aboutLink');

if (location.pathname === '/about'){
    dashboard.className = dashboard.className.replace(" choosen", "");
    about += " choosen";
}else{
    dashboard.className += " choosen";
    about.className = about.className.replace(" choosen", "")

}