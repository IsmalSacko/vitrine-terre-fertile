import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TeamModule } from './team/team.module';
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({


  imports: [
    TypeOrmModule.forRoot({
      type: 'sqlite',
      database: 'database.sqlite',
      autoLoadEntities: true,
      synchronize: true,
    }),
    TeamModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule { }
