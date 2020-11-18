from django.shortcuts import render
from missions.models import Mission, Season
from django.db.models import Count



def missions(request):
    sort_ord = 'id'
    if request.method == 'GET' and 'sort' in request.GET:
        sort_type = request.GET['sort']
        if (sort_type == 'survivors'):
            sort_ord = 'num_players'
        if (sort_type) == 'num_tiles':
            sort_ord = 'tilecount'
        #if (sort_type == 'tiles'):
        #    sort_ord = 'tiles'
        if (sort_type == 'length'):
            sort_ord = 'length_play'
        if (sort_type == 'difficulty'):
            sort_ord = 'difficulty'
        if (sort_type == 'title'):
            sort_ord = 'title'
        if (sort_type == 'title_id'):
            sort_ord = 'title_id'
        if (sort_type == 'season'):
            sort_ord = 'seasons'
    sql_filter = ''
    diff_filter = ''
    if request.method == 'GET' and 'difficulty' in request.GET:
        diff_filter = request.GET['difficulty']
        if len(diff_filter) > 0:
            missioners =  Mission.objects.annotate(tilecount=Count('tiles')).all().filter(difficulty=diff_filter).order_by(sort_ord)
        else:
            missioners = Mission.objects.annotate(tilecount=Count('tiles')).all().order_by(sort_ord)
    else:
        missioners = Mission.objects.annotate(tilecount=Count('tiles')).all().order_by(sort_ord)
    if request.method == 'GET' and 'tileset' in request.GET:
        filter_type = request.GET['tileset']
        sql_filter = filter_type
        if filter_type == 'ALL':
            sql_filter = ''
    if len(sql_filter) > 0:
        missioners = missioners.filter(seasons=Season.objects.all().filter(season=sql_filter).first())

    # Set counts
    s1count = Mission.objects.all().filter(seasons=1).count()
    s2count = Mission.objects.all().filter(seasons=2).count()
    s3count = Mission.objects.all().filter(seasons=3).count()
    tcmcount = Mission.objects.all().filter(seasons=4).count()
    ancount = Mission.objects.all().filter(seasons=5).count()
    zdcount = Mission.objects.all().filter(seasons=6).count()
    dccount = Mission.objects.all().filter(seasons=7).count()

    totcount = Mission.objects.all().count()
    seasonCount = [ str(s1count), str(s2count), str(tcmcount), str(s3count), str(ancount), str(zdcount), str(dccount), str(totcount) ]

    # Set context to the values to pass to the template
    context = {
        'missioners' : missioners,
        'tile_set' : sql_filter,
        'diff_filter' : diff_filter,
        'seasonCount' : seasonCount
    }
    return render(request, 'missions/mission.html', context)
