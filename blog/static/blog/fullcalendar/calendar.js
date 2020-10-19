var initialize_calendar;
var events = JSON.parse(JSON.parse(document.getElementById('events').textContent));
initialize_calendar = function()
{
    $('.calendar').each(function()
        {
            var calendar = $(this);
            calendar.fullCalendar({
                header: {
                    left:'prev,next today',
                    center: 'title',
                    right: 'month, agendaWeek, agendaDay'
                },
                selectable: true,
                selectHelper: true,
                editable: true,
                eventLimit: true,
                firstDay: 1,
                events: events,
                timeFormat: 'h:mm'
            });
        })
};
// $(document).on('turbolinks:load', initialize_calendar);
$(document).ready(function() {
    initialize_calendar();
});