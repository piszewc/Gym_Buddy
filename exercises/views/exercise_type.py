class ExerciseTypeListView(ListView):
    '''
    Overview of all categories, for administration purposes
    '''
    model = ExerciseType
    permission_required = 'exercises.change_exercisetype'

class ExerciseTypeAddView(CreateView):
    '''
    Generic view to add a new exercise type
    '''

    model = ExerciseType
    fields = '__all__'
    success_url = reverse_lazy('exercise:type:list')
    title = ugettext_lazy('Add type')
    form_action = reverse_lazy('exercise:type:add')
    permission_required = 'exercises.add_exercisetype'

    def form_valid(self, form):
        return super(ExerciseTypeAddView, self).form_valid(form)


class ExerciseTypeUpdateView(UpdateView):
    '''
    Generic view to update an existing exercise type
    '''

    model = ExerciseType
    fields = '__all__'
    success_url = reverse_lazy('exercise:type:list')
    permission_required = 'exercises.change_exercisetype'

    # Send some additional data to the template
    def get_context_data(self, **kwargs):
        context = super(ExerciseTypeUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('exercise:type:edit', kwargs={'pk': self.object.id})
        context['title'] = _(u'Edit {0}').format(self.object.name)

        return context

    def form_valid(self, form):
        return super(ExerciseTypeUpdateView, self).form_valid(form)


class ExerciseTypeDeleteView(DeleteView):
    '''
    Generic view to delete an existing exercise type
    '''

    model = ExerciseType
    fields = ('name',)
    success_url = reverse_lazy('exercise:type:list')
    delete_message = ugettext_lazy('This will also delete all exercises in this type.')
    messages = ugettext_lazy('Successfully deleted')
    permission_required = 'exercises.delete_exercisetype' 

    # Send some additional data to the template
    def get_context_data(self, **kwargs):
        context = super(ExerciseTypeDeleteView, self).get_context_data(**kwargs)

        context['title'] = (u'Delete {0}?').format(self.object.name)
        context['form_action'] = reverse('exercise:type:delete', kwargs={'pk': self.object.id})

        return context
