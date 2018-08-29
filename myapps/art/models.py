import osimport uuidfrom django.db import models# Create your models here.from DjangoUeditor.models import UEditorFieldclass Tag(models.Model):    # name,describe,add_time    name = models.CharField(max_length=50)    describe = models.CharField(max_length=255)    add_time = models.DateTimeField(auto_now_add = True,verbose_name='添加')    def __str__(self):        return self.name    class Meta:  #元信息——描述模型类的信息（ORM）        db_table = 't_tag' #类对应数据库中表的名称        verbose_name = '标签'        verbose_name_plural = verbose_name        ordering = ['-add_time']class Category(models.Model):    title = models.CharField(max_length=20,unique=True,verbose_name='标题')    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')    cover = models.ImageField(verbose_name='封面',                              upload_to='category', #相对MEDIA_ROOT                              blank=True,                              null=True,)    parent = models.ForeignKey('self',verbose_name='所属分类'                               ,on_delete=models.SET_NULL,                               null=True,                               blank=True)#后台管理页面中是否为空    def __str__(self):        return self.title    class Meta:        db_table = 't_category'        verbose_name = '分类'        verbose_name_plural = verbose_name        ordering = ['-add_time']def  save_file_path(instance,filename):    #new_file_name = str(uuid.uuid4()).replace('-','')+os.path    new_file_name = str(uuid.uuid4()).replace('-', '') + os.path.splitext(filename)[-1]    return 'arts/{}'.format(new_file_name)class Art(models.Model):    title = models.CharField(max_length=20,unique=True,verbose_name='标签')    content = models.TextField(verbose_name='文章内容')    author = models.CharField(max_length=50,verbose_name='作者')    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')    cate = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类级联')    tag = models.ManyToManyField(Tag,verbose_name='所有标签')    cover = models.ImageField(verbose_name='封面',                              upload_to=save_file_path,  # 相对MEDIA_ROOT                              blank=True,                              null=True,)    def __str__(self):        return self.title    class Meta:        db_table = 't_art'        verbose_name = '文章'        verbose_name_plural = verbose_name        ordering = ['-publish_date']class RollSet(models.Model):    free = ((0,'免费'),(1,'VIP'))    name = models.CharField(max_length=50,unique=True,verbose_name='名称')    free = models.IntegerField(verbose_name='免费级别',choices=free,default=0,)    art = models.ForeignKey(Art,on_delete=models.CASCADE,verbose_name='所属文章')    def __str__(self):        return self.name    @property    def free_name(self):        return self.free[self.free][1]    class Meta:        db_table = 't_roll'        verbose_name = '卷集'        verbose_name_plural = verbose_name        ordering = ['id']class Chapter(models.Model):    name = models.CharField(max_length=80,verbose_name='章节')    content = UEditorField(verbose_name='内容',width=600,height=800,imagePath='ueditor/art/images/',toolbars='mini')    publish_date = models.DateTimeField(auto_now_add=True,                                        verbose_name='发布时间')    rool = models.ForeignKey(RollSet,on_delete=models.CASCADE,verbose_name='所属卷集')    def __str__(self):        return self.name    class Meta:        db_table = 't_chapter'        verbose_name = '章节'        verbose_name_plural = verbose_name        ordering = ['publish_date']