# Generated by Django 4.1.3 on 2022-11-27 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('birh_date', models.DateTimeField()),
                ('image', models.ImageField(default='pic.png', upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='login_registeration_app.gender')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='login_registeration_app.role')),
            ],
        ),
        migrations.CreateModel(
            name='LOL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bool', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='login_registeration_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('followeduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfollowers', to='login_registeration_app.user')),
                ('followinguser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfollowings', to='login_registeration_app.user')),
            ],
        ),
    ]
