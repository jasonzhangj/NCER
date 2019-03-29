# Generated by Django 2.1.7 on 2019-03-27 20:28

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NCER', '0002_auto_20190327_2148'),
        ('Python', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramingQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='题目')),
                ('Answer', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='答案解析')),
                ('Difficulty', models.IntegerField(default=5, verbose_name='难度')),
                ('Disabled', models.BooleanField(default=False, verbose_name='删除')),
                ('CreateTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('CreateBy', models.CharField(blank=True, max_length=50, null=True, verbose_name='创建人')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('ModifyBy', models.CharField(blank=True, max_length=50, null=True, verbose_name='修改人')),
                ('Remark', models.CharField(blank=True, max_length=1000, null=True, verbose_name='备注')),
                ('Level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NCER.Levels', verbose_name='考试分类')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NCER.SubType', verbose_name='类型')),
            ],
            options={
                'verbose_name': '编程题',
                'verbose_name_plural': '编程题',
            },
        ),
        migrations.RemoveField(
            model_name='codequestions',
            name='choicequestions_ptr',
        ),
        migrations.AlterField(
            model_name='choicequestions',
            name='Answer',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='答案解析'),
        ),
        migrations.AlterField(
            model_name='choicequestions',
            name='Desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='题目'),
        ),
        migrations.AlterField(
            model_name='options',
            name='Option',
            field=ckeditor.fields.RichTextField(default='', verbose_name='选项'),
        ),
        migrations.DeleteModel(
            name='CodeQuestions',
        ),
    ]