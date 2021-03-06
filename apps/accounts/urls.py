from django.conf.urls import url
from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^on_site_information/$', views.OnSiteInformationView.as_view(), name='information'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^update_profile/$', views.UpdateProfileView.as_view(), name='update_profile'),
    url(r'^create_team/(?P<challenge_id>[0-9]+)$', views.create_team, name='create_team'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^create_team/success_create_team$', views.success_create_team, name='success_create_team'),
    url(r'^panel/(?P<participation_id>[0-9]+)?$', views.team_management, name='panel'),
    url(r'^panel/accept_participation/(?P<participation_id>[0-9]+)$', views.accept_participation,
        name='accept_participation'),
    url(r'^panel/reject_participation/(?P<participation_id>[0-9]+)$', views.reject_participation,
        name='reject_participation'),
    url(r'^panel/cancel_participation/(?P<participation_id>[0-9]+)/(?P<user_id>[0-9]+)$',
        views.cancel_participation_request, name='cancel_participation_request'),
    url(r'^panel/add_participation/(?P<participation_id>[0-9]+)$', views.add_participation,
        name='add_participation'),
    url(r'^panel/set_final_submission/(?P<submission_id>[0-9]+)', views.set_final_submission,
        name='set final submission'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^email_sent$', views.email_sent, name='email_sent'),
    url(r'^email_confirm$', views.email_confirm, name='email_confirm'),
    url(r'^email_invalid$', views.email_invalid, name='email_invalid'),
    url(r'^challenge_a_team/(?P<participation_id>\d+)$', views.challenge_a_team, name='challenge_a_team'),
    url(r'^panel/phase/(?P<phase_id>\d+)/$', views.render_phase, name='panel_phase'),
    url(r'^panel/(?P<challenge_id>\d+)/scoreboard/$', views.render_scoreboard, name='scoreboard'),
    url(r'^panel/phase/(?P<phase_id>\d+)/(?P<challenge_id>\d+)/scoreboard/$', views.render_phase_scoreboard,
        name='phase_scoreboard'),
    url(r'^panel/phase/(?P<phase_id>\d+)/get_new_trial/$', views.get_new_trial, name='new_trial'),
    url(r'^panel/phase/(?P<phase_id>\d+)/get_new_trial_2/$', views.get_new_trial_phase_2, name='new_trial_phase_2'),
    url(r'^panel/phase/(?P<phase_id>\d+)/trial/(?P<trial_id>\d+)/$', views.render_trial, name='panel_trial'),
    url(r'^panel/phase/(?P<phase_id>\d+)/trial/(?P<trial_id>\d+)/get_dataset$', views.get_dataset, name='get_dataset'),
    url(r'^panel/phase/(?P<phase_id>\d+)/trial/(?P<trial_id>\d+)/get_brands$', views.get_brands, name='get_brands'),
    url(r'^panel/phase/(?P<phase_id>\d+)/trial/(?P<trial_id>\d+)/submit$', views.
        submit_trial, name='submit_trial'),
    url(r'^panel/team/$', views.team_management, name='panel_team_management'),
    url(r'^panel/teampc/(?P<team_pc>\d+)$', views.change_team_pc, name='panel_change_team_pc'),
    url(r'^panel/phase/(?P<phase_id>\d+)/set_final_trial/(?P<trial_id>\d+)/$', views.set_final_trial,
        name='set_final_trial'),
    url(r'^panel/notifications/$', views.get_notification, name='panel_notifications'),


    url(r'^judge/(?P<phase_id>\d+)$', views.manual_judge, name='manual_judge'),
    url(r'^judge/get_download_link/$', views.get_download_link, name='judge_download_link'),
    url(r'^judge/set_score/$', views.set_trial_score_manually, name='manual_score'),

]
