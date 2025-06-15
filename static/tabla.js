$(document).ready(function() {
    // Verifica y destruye inicializaciones anteriores
    if ($.fn.DataTable.isDataTable('#tabla_disponibles')) {
        $('#tabla_disponibles').DataTable().destroy();
    }
    if ($.fn.DataTable.isDataTable('#tabla_eliminados')) {
        $('#tabla_eliminados').DataTable().destroy();
    }

    // Inicializa tabla de disponibles ordenada descendentemente por "codigo"
    $('#tabla_disponibles').DataTable({
        language: {
            url: "//cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json"
        },
        responsive: true,
        dom: '<"top"lf>rt<"bottom"ip><"clear">',
        order: [[0, 'desc']], // Columna 0 = código
        columnDefs: [
            {
                targets: [7], // columna "Acciones"
                orderable: false,
                searchable: false,
                className: "dt-center"
            }
        ]
    });

    // Inicializa tabla de eliminados, también puedes ordenar por código
    $('#tabla_eliminados').DataTable({
        language: {
            url: "//cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json"
        },
        responsive: true,
        dom: '<"top"lf>rt<"bottom"ip><"clear">',
        order: [[0, 'desc']], // orden por código (columna 0)
        columnDefs: [
            {
                targets: [8], // columna "Acciones"
                orderable: false,
                searchable: false,
                className: "dt-center"
            }
        ]
    });
});